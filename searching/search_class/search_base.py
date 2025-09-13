from abc import ABCMeta, abstractmethod


class search_base(metaclass=ABCMeta):
    __slots__ = "_verbose"

    def __init__(self, verbose: bool) -> None:
        self._verbose = verbose
        pass

    @abstractmethod
    def execute(self, arr: list[int]) -> bool:
        pass
