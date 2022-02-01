import time
import colorsys

from inkydev import InkyDev


inkydev = InkyDev()

while True:
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        print(f"Buttons A {button_a} B {button_b} C {button_c} D {button_d}")

    time.sleep(0.001)
