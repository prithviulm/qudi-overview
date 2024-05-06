"""
This module contains the hardware class that will be used to interface with various
hardware in experiments.
"""

import numpy as np
from abc import ABC, abstractmethod
import logging
import warnings

SEED = 42
np.random.seed(SEED)

logger = logging.getLogger(__name__)


class Hardware(ABC):
    """
    This base class contains the minimum functionality required of all hardware
    devices.

    ********************************************
    *** DO NOT MODIFY ANYTHING IN THIS CLASS ***
    ********************************************

    """

    @abstractmethod
    def status(self) -> bool:
        """
        A boolean indicating whether the hardware device is connected or not.
        """

        pass

    @abstractmethod
    def connect(self) -> None:
        """
        Connects to the hardware device.
        """

        pass

    @abstractmethod
    def disconnect(self) -> None:
        """
        Disconnects from the hardware device.
        """

        pass

    @abstractmethod
    def acquire(self, time: int | float) -> int | float | list[int | float]:
        """
        Acquires data from the hardware device for a given amount of time.

        Parameters
        ----------
        time : int | float
            The amount of time in seconds to acquire data for.

        Returns
        -------
        data : int | float | list[int | float]
            The data acquired from the hardware device.
        """

        pass


class APD(Hardware):
    """
    This class represents an Avalanche Photodiode (APD) detector. It detects and counts
    single photons of light.
    """

    _default_integration_time: int | float = 0.1

    def __init__(
        self, integration_time: int | float = _default_integration_time
    ) -> None:
        """
        Initializes the APD.

        Parameters
        ----------
        integration_time : int | float, optional
            The integration time of the APD in seconds.
        """

        self.integration_time = float(integration_time)
        self.__connected = False

    @property
    def integration_time(self) -> float:
        """
        Returns the integration time of the APD.
        """

        return self.__integration_time

    @integration_time.setter
    def integration_time(self, value: int | float) -> None:
        """
        Sets the integration time of the APD.

        Parameters
        ----------
        value : int | float
            The integration time in seconds.
        """

        if not isinstance(value, int | float):
            raise TypeError("Integration time must be a positive int or float.")

        if value <= 0:
            raise ValueError("Integration time must be greater than zero.")

        self.__integration_time = float(value)

    def connect(self) -> None:
        """
        Connects to the APD.
        """

        if not self.__connected:
            self.__connected = True
            logger.info("Connected to APD.")
        else:
            warnings.warn("APD is already connected.")

    def disconnect(self) -> None:
        """
        Disconnects from the APD.
        """

        if self.__connected:
            self.__connected = False
            logger.info("Disconnected from APD.")
        else:
            warnings.warn("APD is already disconnected.")

    def acquire(self, integration_time: int | float = None) -> int:
        """
        Acquires counts from the APD for a given amount of time.

        Parameters
        ----------
        integration_time : int | float, optional
            The amount of time in seconds to acquire counts for in this acquisition.
            This DOES NOT change the integration time of subsequent acquisitions (see
            integration_time attribute for that). If None, the value when the class was
            initialised is used.

        Returns
        -------
        counts : int
            The number of counts detected by the APD over the integration time.
        """

        if self.status() is False:
            raise ConnectionError("APD is not connected.")

        if integration_time is None:
            integration_time = self.integration_time

        counts = np.random.poisson(1e4 * integration_time)

        return counts
