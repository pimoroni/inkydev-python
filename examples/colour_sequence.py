#!/usr/bin/env python3

import time
import atexit

from inkydev import InkyDev

inkydev = InkyDev()

colours = [
    (255, 0, 0),
    (255, 255, 0),
    (0, 255, 0),
    (0, 255, 255),
    (0, 0, 255),
    (255, 0, 255)
]
current = 0


def exit():
    inkydev.clear()
    inkydev.update()


atexit.register(exit)

while True:
    r, g, b = colours[current]

    for i in range(4):
        inkydev.set_led(i, r, g, b, brightness=0.1)

    current += 1
    if current == len(colours):
        current = 0

    inkydev.update()
    print(f"{r:02X}{g:02X}{b:02X}")
    time.sleep(1.0)
