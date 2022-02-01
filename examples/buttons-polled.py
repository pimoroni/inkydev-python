import time

from inkydev import InkyDev


inkydev = InkyDev()

while True:
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        print(f"Buttons - A: {button_a} B: {button_b} C: {button_c} D: {button_d}")
        inkydev.set_led(0, 255 * button_a, 0, 0)
        inkydev.set_led(1, 0, 255 * button_b, 0)
        inkydev.set_led(2, 0, 0, 255 * button_c)
        inkydev.set_led(3, 255 * button_d, 0, 255 * button_d)
        inkydev.update()

    time.sleep(0.001)
