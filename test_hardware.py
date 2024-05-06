import hardware


def test_apd_connect() -> None:
    """
    Test that the APD can be connected.
    """

    apd = hardware.APD()
    apd.connect()
    assert apd.status() is True


def test_apd_integration_time() -> None:
    """
    Test that the integration time of the APD can be set and retrieved.
    """

    # Your code here

    pass


def test_your_function() -> None:
    """
    Create a test that you think is important.
    """

    # Your code here

    pass
