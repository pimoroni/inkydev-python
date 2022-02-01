import sys
import mock
import pytest


@pytest.fixture(scope='function', autouse=False)
def smbus2():
    """Mock smbus module."""
    sys.modules['smbus2'] = mock.MagicMock()
    yield sys.modules['smbus2']
    del sys.modules['smbus2']


@pytest.fixture(scope='function', autouse=False)
def inkydev():
    """Import scd4x module."""
    import inkydev
    yield inkydev
    del sys.modules['inkydev']
