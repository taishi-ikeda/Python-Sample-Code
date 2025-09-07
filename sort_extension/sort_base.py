from abc import ABCMeta, abstractmethod


class order_func_base(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get(x: int) -> int:
        pass


class sort_base(metaclass=ABCMeta):
    def __init__(self, verbose: bool, func: order_func_base) -> None:
        self._verbose = verbose
        self._step_counter = 0
        self._func = func
        pass

    @abstractmethod
    def execute(self, arr: list[int], func: order_func_base) -> list[int]:
        pass

    def check_sort(self, li: list[int]) -> bool:
        for i in range(0, len(li) - 1):
            if self._func.get(li[i]) > self._func.get(li[i + 1]):
                return False
        return True
