"""Test configuration.
These allow the mocking of various Python modules
that might otherwise have runtime side-effects.
"""
import sys
import mock
import pytest


@pytest.fixture(scope='function', autouse=True)
def cleanup():
    yield None
    try:
        del sys.modules['pibrella']
    except KeyError:
        pass


@pytest.fixture(scope='function', autouse=False)
def GPIO():
    """Mock RPi.GPIO module."""
    GPIO = mock.MagicMock()
    # Fudge for Python < 37 (possibly earlier)
    sys.modules['RPi'] = mock.Mock()
    sys.modules['RPi'].GPIO = GPIO
    sys.modules['RPi.GPIO'] = GPIO
    yield GPIO
    del sys.modules['RPi']
    del sys.modules['RPi.GPIO']


@pytest.fixture(scope='function', autouse=False)
def atexit():
    """Mock atexit module."""
    atexit = mock.MagicMock()
    sys.modules['atexit'] = atexit
    yield atexit
    del sys.modules['atexit']