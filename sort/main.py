import sort_merge as sm
import sort_bubble as sb
import random

arr = [random.randint(0,100) for i in range(30)]
print(arr)
SortMerge = sm.merge_sort(True)
arr_merge=SortMerge.execute(arr)
print(arr_merge)

SortBubble = sb.merge_bubble(True)
arr_bubble = SortBubble.execute(arr)
print(arr_bubble)
print(arr)
