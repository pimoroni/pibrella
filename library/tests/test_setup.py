import pytest


def test_setup_attaches_atexit_handler(GPIO, atexit):
    import pibrella

    assert atexit.atexit.called_once_with(pibrella.pibrella_exit)


def test_setup_initializes_gpio(GPIO, atexit):
    import pibrella

    assert GPIO.setmode.called_once_with(GPIO.BCM)
    assert GPIO.setwarnings.called_once_with(False)

    assert GPIO.setup.called_once_with(pibrella.PB_PIN_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)