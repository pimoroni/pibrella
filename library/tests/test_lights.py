import pytest
import mock


def test_pibrella_red_light_on(GPIO, atexit):
    import pibrella

    pibrella.light.red.on()
    pibrella.light.red.off()

    assert GPIO.output.has_calls((
        mock.call(pibrella.PB_PIN_LIGHT_RED, True),
        mock.call(pibrella.PB_PIN_LIGHT_RED, False)
    ))