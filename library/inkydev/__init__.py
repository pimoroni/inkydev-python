import smbus2


__version__ = '0.0.1'


I2C_ADDRESS = 0x3b
REG_INPUT = 0x00
REG_OUTPUT = 0x01
REG_POLARITY = 0x02
REG_CONFIG = 0x03
LED_FRAME = 0xE0000000

LED_CLK = 0b10000000
LED_CLK = 0b01000000
LED_PWR_EN = 0b00010000
EPD_PWR_EN = 0b00100000

BUTTON_A = 0b00000001
BUTTON_B = 0b00000010
BUTTON_C = 0b00000100
BUTTON_D = 0b00001000

PIN_INTERRUPT = 4


class InkyDev:
    def __init__(self, i2c_bus=None):
        if i2c_bus is None:
            i2c_bus = smbus2.SMBus(1)
        self._i2c = i2c_bus

        self._i2c.write_byte_data(I2C_ADDRESS, REG_CONFIG, 0x0F)
        self._i2c.write_byte_data(I2C_ADDRESS, REG_POLARITY, 0x00)
        self._i2c.write_byte_data(I2C_ADDRESS, REG_OUTPUT, 0x00)

        self._leds = [(20, 0, 0, 0) for _ in range(4)]

        self._epd_power = True

        # Pre-bake the register writes for the start/end frames because they never change
        self._start_frame = self.prepare_frame(0x00000000)
        self._end_frame = self.prepare_frame(0xFFFFFFFF)
        self._last_buttons = 0

    def chunk(self, data, chunksize):
        """Split a list of values in to chunks of length n."""
        for i in range(0, len(data) + 1, chunksize):
            yield data[i:i + chunksize]

    def set_epd_power(self, value):
        self._epd_power = value
        self._i2c.write_byte_data(I2C_ADDRESS, REG_OUTPUT, 0x00 if value else EPD_PWR_EN)

    def read_buttons(self):
        buttons = self._i2c.read_byte_data(I2C_ADDRESS, REG_INPUT)
        button_a = (buttons & BUTTON_A) == 0
        button_b = buttons & BUTTON_B == 0
        button_c = buttons & BUTTON_C == 0
        button_d = buttons & BUTTON_D == 0
        changed = buttons != self._last_buttons
        self._last_buttons = buttons
        return button_a, button_b, button_c, button_d, changed

    def prepare_frame(self, frame):
        """Convert a single 32bit LED frame into a sequence of output register writes."""
        data = []
        for _ in range(32):
            if frame & (1 << 31):
                # Clock LOW + set data bit, followed by clock HIGH
                data += [0b01000000, 0b11000000]
            else:
                # Clock LOW + clear data bit, followed by clock HIGH
                data += [0b00000000, 0b10000000]
            frame <<= 1

        if not self._epd_power:
            data = [d | EPD_PWR_EN for d in data]

        return data

    def update(self):
        data = []
        data += self._start_frame
        for led in self._leds:
            brightness, r, g, b = led
            led_frame = LED_FRAME | (brightness << 24) | (b << 16) | (g << 8) | r
            data += self.prepare_frame(led_frame)
        data += self._end_frame

        for c in self.chunk(data, 32):
            self._i2c.write_i2c_block_data(I2C_ADDRESS, REG_OUTPUT, c)

    def clear(self):
        for i in range(4):
            self.set_led(i, 0, 0, 0, brightness=1.0)

    def set_led(self, i, r, g, b, brightness=None):
        if brightness is None:
            brightness = self._leds[i][0]
        else:
            brightness = int(31 * brightness)
        self._leds[i] = (brightness, r, g, b)
