from abc import ABCMeta, abstractmethod


class search_base(metaclass=ABCMeta):
    __slots__ = "_verbose"

    def __init__(self, verbose: bool) -> None:
        self._verbose = verbose
        pass

    @abstractmethod
    def find(self, arr: list[int]) -> bool:
        pass

    @abstractmethod
    def append(self, x: int)->None:
        pass
