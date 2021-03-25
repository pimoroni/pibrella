import pytest
import mock


def test_pibrella_output_a_on(GPIO, atexit):
    import pibrella

    pibrella.output.e.on()
    pibrella.output.e.off()

    assert GPIO.output.has_calls((
        mock.call(pibrella.PB_PIN_OUTPUT_A, True),
        mock.call(pibrella.PB_PIN_OUTPUT_A, False)
    ))