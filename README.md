# Inky Development Board

[![Build Status](https://img.shields.io/github/actions/workflow/status/pimoroni/inkydev-python/test.yml?branch=main)](https://github.com/pimoroni/inkydev-python/actions/workflows/test.yml)
[![Coverage Status](https://coveralls.io/repos/github/pimoroni/inkydev-python/badge.svg?branch=master)](https://coveralls.io/github/pimoroni/inkydev-python?branch=master)
[![PyPi Package](https://img.shields.io/pypi/v/inkydev.svg)](https://pypi.python.org/pypi/inkydev)
[![Python Versions](https://img.shields.io/pypi/pyversions/inkydev.svg)](https://pypi.python.org/pypi/inkydev)

# Pre-requisites

You must enable:

* i2c: `sudo raspi-config nonint do_i2c 0`
* spi: `sudo raspi-config nonint do_spi 0`

You can optionally run `sudo raspi-config` or the graphical Raspberry Pi Configuration UI to enable interfaces.

# Installing

Stable library from PyPi:

* Just run `pip3 install inkydev`

In some cases you may need to use `sudo` or install pip with: `sudo apt install python3-pip`

Latest/development library from GitHub:

* `git clone https://github.com/pimoroni/inkydev-python`
* `cd inkydev-python`
* `sudo ./install.sh`

