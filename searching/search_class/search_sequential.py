from . import search_base


class sequential_search(search_base.search_base):
    __slots__ = ()

    def __init__(self, verbose: bool) -> None:
        super().__init__(verbose)

    def execute(self, arr: list[int], x: int) -> bool:
        for i in range(len(arr)):
            if arr[i] == x:
                return True
        return False
