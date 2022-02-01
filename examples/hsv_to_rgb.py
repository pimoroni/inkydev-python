import time
import colorsys
import atexit

from inkydev import InkyDev


"""
For a 50FPS framerate, set the following in /boot/config.txt:

dtparam=i2c_arm=on,i2c_arm_baudrate=400000
"""


frames = 0
time_start = time.time()
time_last = time.time()

inkydev = InkyDev()


def exit():
    inkydev.clear()
    inkydev.update()


atexit.register(exit)

while True:
    t = time.time()

    for i in range(4):
        h = t * 100
        h += 90 * i
        h /= 360.0
        r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
        inkydev.set_led(i, r, g, b, brightness=0.1)

    inkydev.update()

    frames += 1
    if t - time_last >= 2.0:
        time_elapsed = t - time_start
        print(f"{frames / time_elapsed:2.2f} FPS")
        time_last = time.time()
