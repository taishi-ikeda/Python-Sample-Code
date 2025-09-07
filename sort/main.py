import sort_class.sort_merge as sm
import sort_class.sort_bubble as sb
import sort_class.sort_quick as sp
import sort_class.sort_selection as ss
import sort_class.sort_insertion as si
import sort_class.sort_shell as ssh
import sort_class.sort_heap as sh
import sort_class.sort_heap2 as sh2
import random

arr = [random.randint(-100, 100) for i in range(20)]
print(arr)
SortMerge = sm.merge_sort(False)
arr_merge = SortMerge.execute(arr)
print(arr_merge)

SortBubble = sb.bubble_sort(False)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

SortQuick = sp.quick_sort(False,"random")
arr_quick = SortQuick.execute(arr)
print(arr_quick)

SortSelection = ss.selection_sort(False)
arr_selection = SortSelection.execute(arr)
print(arr_selection)

SortInsertion = si.insertion_sort(False)
arr_insertion = SortInsertion.execute(arr)
print(arr_insertion)

SortShell = ssh.shell_sort(False)
arr_shell = SortShell.execute(arr)
print(arr_shell)

SortHeap = sh.heap_sort(False, 1000)
arr_heap = SortHeap.execute(arr)
print(arr_heap)

SortHeap2 = sh2.heap_sort2(False)
arr_heap2 = SortHeap2.execute(arr)
print(arr_heap2)
