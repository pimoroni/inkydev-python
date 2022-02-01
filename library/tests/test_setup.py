def test_setup(smbus2, inkydev):
    dev = inkydev.InkyDev()
    smbus2.SMBus.called_once_with(1)
    del dev
