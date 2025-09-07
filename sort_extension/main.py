import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_heap as sh
import sort_heap2 as sh2
import sort_insertion as si
import sort_selection as ss
import sort_shell as ssh
import sort_base
import random


class opposite_order(sort_base.order_func_base):
    def __init__(self) -> None:
        pass

    def get(self, x: int) -> int:
        return -x


if __name__ == "__main__":
    func = opposite_order()
    arr = [random.randint(0, 100) for i in range(30)]
    print(arr)
    SortMerge = sm.merge_sort(False, func)
    arr_merge = SortMerge.execute(arr)
    print(arr_merge)

    SortBubble = sb.merge_bubble(False, func)
    arr_bubble = SortBubble.execute(arr)
    print(arr_bubble)

    SortQuick = sp.quick_sort(False, "random",func)
    arr_quick = SortQuick.execute(arr)
    print(arr_quick)

    SortInsertion = si.insertion_sort(False, func)
    arr_insertion = SortInsertion.execute(arr)
    print(arr_insertion)

    SortSelection = ss.selection_sort(False, func)
    arr_selection = SortSelection.execute(arr)
    print(arr_selection)

    SortShell = ssh.shell_sort(False, func)
    arr_shell = SortShell.execute(arr)
    print(arr_shell)

    SortHeap = sh.heap_sort(False, 1000, func)
    arr_heap = SortHeap.execute(arr)
    print(arr_heap)

    SortHeap2 = sh2.heap_sort2(False, func)
    arr_heap2 = SortHeap2.execute(arr)
    print(arr_heap2)
