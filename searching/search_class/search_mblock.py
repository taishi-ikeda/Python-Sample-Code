from . import search_base
import sort.sort_class.sort_factory as sf
import math


class mblock_search(search_base.search_base):
    __slots__ = ("_sort",
                 "_data",
                 "_m_block")

    def __init__(self, verbose: bool,
                 sort_method: str = "quick",
                 m_block:int=-1) -> None:
        super().__init__(verbose)
        self._sort = sf.sort_factory.create(sort_method)
        self._data = []

    def append(self,x:int):
        self._data.append(x)

    def find(self, x: int, m_block: int = -1) -> bool:
        size = len(self._data)
        if m_block == -1:
            m_block = int(math.sqrt(size))
        sorted_arr = self._sort.execute(self._data)

        if self._verbose:
            print(sorted_arr)

        max_ele_num = int(size / m_block) + 1
        ele_num = max_ele_num
        ele_num_last = size - ele_num * (m_block - 1)
        if self._verbose:
            print("ele_num = ", ele_num)
        if sorted_arr[size - 1] < x:
            return False

        target_block = -1
        for ib in range(0, m_block - 1):
            j = (ib + 1) * ele_num - 1
            if x <= sorted_arr[j]:
                target_block = ib
                break
        if target_block == -1:
            target_block = m_block - 1

        if not target_block == m_block - 1:
            if self._verbose:
                print(
                    "target_block ; ",
                    sorted_arr[target_block * ele_num : (target_block + 1) * ele_num],
                )
            for i in range(target_block * ele_num, (target_block + 1) * ele_num):
                if x <= sorted_arr[i]:
                    break
            if sorted_arr[i] == x:
                return True
            return False
        else:
            if self._verbose:
                print("target_block ; ", sorted_arr[target_block * ele_num : size])
            for i in range(target_block * ele_num, size):
                if x <= sorted_arr[i]:
                    break
            if sorted_arr[i] == x:
                return True
            return False
