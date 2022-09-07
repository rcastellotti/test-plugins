from abc import ABCMeta, abstractmethod


class PluginBase(metaclass=ABCMeta):
    """Base class for plugins"""


    @abstractmethod
    def print(self) -> None:
        """prints some stuff"""

