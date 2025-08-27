import unittest
import sort_merge as sm
import sort_bubble as sb
import sort_quick as sp

class TestSort(unittest.TestCase):
    def test_sort1(self):
        arr=[30,1,5,7,3,29,8,10]

        SortMerge = sm.merge_sort(False)
        arr_merge=SortMerge.execute(arr)

        SortBubble = sb.merge_bubble(False)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False)
        arr_quick = SortQuick.execute(arr)

        expected = [1,3,5,7,8,10,29,30]
        self.assertEqual(expected,arr_merge)
        self.assertEqual(expected,arr_bubble)
        self.assertEqual(expected,arr_quick)

    def test_sort2(self):
        arr=[30,1,5,7,3,29,8,5,-3]

        SortMerge = sm.merge_sort(False)
        arr_merge=SortMerge.execute(arr)

        SortBubble = sb.merge_bubble(False)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False)
        arr_quick = SortQuick.execute(arr)

        expected = [-3,1,3,5,5,7,8,29,30]
        self.assertEqual(expected,arr_merge)
        self.assertEqual(expected,arr_bubble)
        self.assertEqual(expected,arr_quick)



if __name__== "__main__":
    unittest.main()



