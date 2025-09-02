import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_selection as ss
import sort_insertion as si
import sort_shell as ssh
import sort_heap as sh
import random

arr = [5,4,8,1,3,2,7,6]

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

print("merge sort")
SortMerge = sm.merge_sort(False)
arr_merge=SortMerge.execute(arr)
print(arr_merge)


SortQuick = sp.quick_sort(False)
arr_quick = SortQuick.execute(arr)
print(arr_quick)


SortShell = ssh.shell_sort(False)
arr_shell = SortShell.execute(arr)
print(arr_shell)

SortHeap = sh.heap_sort(False,1000)
arr_heap = SortHeap.execute(arr)
print(arr_heap)





