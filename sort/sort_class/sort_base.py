from abc import ABCMeta, abstractmethod


class sort_base(metaclass=ABCMeta):
    __slots__ = ("_verbose", "_step_counter")

    def __init__(self, verbose: bool) -> None:
        self._verbose = verbose
        self._step_counter = 0
        pass

    @abstractmethod
    def execute(self, arr: list[int]) -> list[int]:
        pass

    def check_sort(self, li: list[int]) -> bool:
        for i in range(0, len(li) - 1):
            if li[i] > li[i + 1]:
                return False
        return True
