import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_selection as ss
import random

arr = [random.randint(0,100) for i in range(30)]
print(arr)
SortMerge = sm.merge_sort(True)
arr_merge=SortMerge.execute(arr)
print(arr_merge)

SortBubble = sb.bubble_sort(True)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)

SortQuick = sp.quick_sort(True)
arr_quick = SortQuick.execute(arr)
print(arr_quick)

SortSelection = ss.selection_sort(False)
arr_selection = SortSelection.execute(arr)
print(arr_selection)



print(arr)
