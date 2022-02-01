#!/usr/bin/env python3

import signal

from inkydev import InkyDev, PIN_INTERRUPT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

inkydev = InkyDev()


def handle_interrupt(pin):
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        print(f"Buttons - A: {button_a} B: {button_b} C: {button_c} D: {button_d}")
        inkydev.set_led(0, 255 * button_a, 0, 0)
        inkydev.set_led(1, 0, 255 * button_b, 0)
        inkydev.set_led(2, 0, 0, 255 * button_c)
        inkydev.set_led(3, 255 * button_d, 0, 255 * button_d)
        inkydev.update()


GPIO.add_event_detect(PIN_INTERRUPT, GPIO.FALLING, callback=handle_interrupt)

signal.pause()
