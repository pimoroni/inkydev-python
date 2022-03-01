import signal

from inky import InkyUC8159
from inkydev import InkyDev, PIN_INTERRUPT
import RPi.GPIO as GPIO

from PIL import Image, ImageFont, ImageDraw
from font_hanken_grotesk import HankenGroteskBold, HankenGroteskMedium
from font_intuitive import Intuitive


SCALE = 1.0
WIDTH = 600
HEIGHT = 448


GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

inkydev = InkyDev()
inkydev.set_epd_power(True)
display = InkyUC8159(resolution=(WIDTH, HEIGHT))

image = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

intuitive_font = ImageFont.truetype(Intuitive, int(22 * SCALE))
hanken_bold_font = ImageFont.truetype(HankenGroteskBold, int(35 * SCALE))
hanken_medium_font = ImageFont.truetype(HankenGroteskMedium, int(16 * SCALE))


def handle_interrupt(pin):
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        draw.rectangle((0, 0, WIDTH, HEIGHT), display.WHITE)

        if button_a:
            draw.text((0, 0), "Button A", display.BLACK, font=intuitive_font)
        if button_b:
            draw.text((0, 0), "Button B", display.BLACK, font=intuitive_font)
        if button_c:
            draw.text((0, 0), "Button C", display.BLACK, font=intuitive_font)
        if button_d:
            draw.text((0, 0), "Button D", display.BLACK, font=intuitive_font)

        inky_display.set_image(image)
        inky_display.show()


GPIO.add_event_detect(PIN_INTERRUPT, GPIO.FALLING, callback=handle_interrupt)

signal.pause()