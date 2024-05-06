"""
This module handles the acquisition of data from various hardware devices. It is
designed to be hardware-agnostic.
"""

import hardware
import logging

logger = logging.getLogger(__name__)


def get_data_vs_time(
    device: hardware.Hardware,
    time: int | float
) -> tuple[list[int], list[float]]:
    """
    Acquires data from the hardware for a given amount of time.

    Parameters
    ----------
    device : hardware.Hardware
        The instantiated device to acquire data from.
    time : int | float
        The total amount of time in seconds to acquire data for. The number of data
        points acquired is determined by this time divided by the integration time of
        the hardware (rounded up to the nearest integer).

    Returns
    -------
    data : list[int]
        The data acquired from the hardware device.
    timestamps : list[float]
        The timestamps in seconds at which the data were acquired.
    """

    if not isinstance(device, hardware.Hardware):
        raise TypeError("device must be an instance of hardware.Hardware.")

    if not isinstance(time, int | float):
        raise TypeError("time must be an int or float.")

    if time <= device.integration_time:
        raise ValueError(
            "time must be greater than the integration time of the device."
        )

    data = []
    timestamps = []
    time_step = device.integration_time

    # Get the first data points
    data.append(device.acquire())
    timestamps.append(time_step)

    # Get the rest of the data points
    while timestamps[-1] + time_step < time:
        data.append(device.acquire())
        timestamps.append(timestamps[-1] + time_step)

    return data, timestamps
