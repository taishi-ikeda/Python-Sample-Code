import sort_class as sort
import random

arr = [random.randint(0,100) for i in range(30)]
print(arr)
Sort = sort.merge_sort(True)
arr_sort=Sort.execute(arr)
print(arr_sort)
