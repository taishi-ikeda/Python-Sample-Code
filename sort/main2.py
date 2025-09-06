import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_selection as ss
import sort_insertion as si
import sort_shell as ssh
import sort_heap as sh
import sort_heap2 as sh2
import random

arr = [5, 4, 8, 1, 3, 2, 7, 6]

print(arr)
print("bubble sort")
SortBubble = sb.bubble_sort(True)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

print("selection sort")
SortSelection = ss.selection_sort(True)
arr_selection = SortSelection.execute(arr)
print(arr_selection)

print("insertion sort")
SortInsertion = si.insertion_sort(True)
arr_insertion = SortInsertion.execute(arr)
print(arr_insertion)

print("shell sort")
SortShell = ssh.shell_sort(True)
arr_shell = SortShell.execute(arr)
print(arr_shell)

print("heap sort")
SortHeap = sh.heap_sort(True, 10)
arr_heap = SortHeap.execute(arr)
print(arr_heap)

print("heap sort2")
SortHeap2 = sh2.heap_sort2(True)
arr_heap2 = SortHeap2.execute(arr)
print(arr_heap2)

print("quick sort")
SortQuick = sp.quick_sort(True,"head")
arr_quick = SortQuick.execute(arr)
print(arr_quick)

print("merge sort")
SortMerge = sm.merge_sort(False)
arr_merge = SortMerge.execute(arr)
print(arr_merge)



