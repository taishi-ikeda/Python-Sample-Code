import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_heap as sh
import sort_base
import random

class opposite_order(sort_base.order_func_base):
    def __init__(self)->None:
        pass
    def get(self,x:int)->int:
        return -x


if __name__ == "__main__":
    func = opposite_order()
    arr = [random.randint(0,100) for i in range(30)]
    print(arr)
    SortMerge = sm.merge_sort(True,func)
    arr_merge=SortMerge.execute(arr)
    print(arr_merge)

    SortBubble = sb.merge_bubble(True,func)
    arr_bubble = SortBubble.execute(arr)
    print(arr_bubble)

    SortQuick = sp.quick_sort(True,func)
    arr_quick = SortQuick.execute(arr)
    print(arr_quick)

    SortHeap = sh.heap_sort(True,1000,func)
    arr_heap = SortHeap.execute(arr)
    print(arr_heap)




