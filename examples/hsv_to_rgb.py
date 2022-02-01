import time
import colorsys

from inkydev import InkyDev


frames = 0
time_start = time.time()
time_last = time.time()

inkydev = InkyDev()

while True:
    t = time.time()

    for i in range(4):
        h = t * 100
        h += 90 * i
        h /= 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        inkydev.set_led(i, r, g, b, brightness=0.1)

    inkydev.update()
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        print(f"Buttons A {button_a} B {button_b} C {button_c} D {button_d}")

    frames += 1
    if t - time_last >= 2.0:
        time_elapsed = t - time_start
