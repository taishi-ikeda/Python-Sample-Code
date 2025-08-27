import unittest
import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp
import sort_base

class opposite_order(sort_base.order_func_base):
    def __init__(self)->None:
        pass
    def get(self,x:int)->int:
        return -x

class TestSort(unittest.TestCase):
    def test_sort1(self):
        func = opposite_order()
        arr=[30,1,5,7,3,29,8,10]

        SortMerge = sm.merge_sort(False,func)
        arr_merge=SortMerge.execute(arr)

        SortBubble = sb.merge_bubble(False,func)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False,func)
        arr_quick = SortQuick.execute(arr)


        expected = [30,29,10,8,7,5,3,1]
        self.assertEqual(expected,arr_merge)
        self.assertEqual(expected,arr_bubble)
        self.assertEqual(expected,arr_quick)

    def test_sort2(self):
        func = opposite_order()
        arr=[30,1,5,7,3,29,8,5,-3]

        SortMerge = sm.merge_sort(False,func)
        arr_merge=SortMerge.execute(arr)

        SortBubble = sb.merge_bubble(False,func)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False,func)
        arr_quick = SortQuick.execute(arr)

        expected = [30,29,8,7,5,5,3,1,-3]
        self.assertEqual(expected,arr_merge)
        self.assertEqual(expected,arr_bubble)
        self.assertEqual(expected,arr_quick)



if __name__== "__main__":
    unittest.main()



