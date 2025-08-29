import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_selection as ss
import sort_insertion as si
import sort_shell as ssh
import sort_heap as sh
import random

arr = [random.randint(-100,100) for i in range(10)]
print(arr)
SortMerge = sm.merge_sort(False)
arr_merge=SortMerge.execute(arr)
print(arr_merge)

SortBubble = sb.bubble_sort(False)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

SortQuick = sp.quick_sort(False)
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

SortHeap = sh.heap_sort(False,1000)
arr_heap = SortHeap.execute(arr)
print(arr_heap)





