import hardware
import pytest

@pytest.fixture(autouse=True)
def apd():
    my_apd = hardware.APD()
    yield my_apd


def test_apd_connect(apd: hardware.APD) -> None:
    """
    Test that the APD can be connected.
    """

    apd.connect()
    assert apd.status() is True


def test_apd_integration_time(apd: hardware.APD) -> None:
    """
    Test that the integration time of the APD can be set and retrieved.
    """

    apd.integration_time = 123.456

    assert apd.integration_time == 123.456

@pytest.mark.parametrize("input", ['notAIntOfFloat'])
def test_exception_is_thrown_when_trying_to_set_invalid_integration_time(apd: hardware.APD, input) -> None:
    """
    Create a test that you think is important.
    """

    # Your code here
    with(pytest.raises(TypeError)):
        apd.integration_time = input


