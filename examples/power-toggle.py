#!/usr/bin/env python3

import signal

from inkydev import InkyDev, PIN_INTERRUPT
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_INTERRUPT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

inkydev = InkyDev()
power = False


def handle_interrupt(pin):
    global power
    button_a, button_b, button_c, button_d, changed = inkydev.read_buttons()

    if changed:
        if button_a:
            if not power:
                inkydev.set_epd_power(True)
                inkydev.set_led(0, 0, 255, 0)
                power = True
            else:
                inkydev.set_epd_power(False)
                inkydev.set_led(0, 255, 0, 0)
                power = False
        inkydev.update()


GPIO.add_event_detect(PIN_INTERRUPT, GPIO.FALLING, callback=handle_interrupt)

inkydev.clear()
inkydev.set_led(0, 255, 0, 0)
inkydev.update()
inkydev.set_epd_power(False)

signal.pause()
