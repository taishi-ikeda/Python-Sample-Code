import unittest
import sort_class.sort_merge as sm
import sort_class.sort_bubble as sb
import sort_class.sort_quick as sp
import sort_class.sort_selection as ss
import sort_class.sort_heap as sh
import sort_class.sort_heap2 as sh2


class TestSort(unittest.TestCase):
    def test_sort1(self):
        arr = [30, 1, 5, 7, 3, 29, 8, 10]

        SortMerge = sm.merge_sort(False)
        arr_merge = SortMerge.execute(arr)

        SortBubble = sb.bubble_sort(False)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False,"random")
        arr_quick = SortQuick.execute(arr)

        SortSelection = ss.selection_sort(False)
        arr_selection = SortSelection.execute(arr)

        SortHeap = sh.heap_sort(False, 100)
        arr_heap = SortHeap.execute(arr)

        SortHeap2 = sh2.heap_sort2(False)
        arr_heap2 = SortHeap2.execute(arr)

        expected = [1, 3, 5, 7, 8, 10, 29, 30]
        self.assertEqual(expected, arr_merge)
        self.assertEqual(expected, arr_bubble)
        self.assertEqual(expected, arr_quick)
        self.assertEqual(expected, arr_selection)
        self.assertEqual(expected, arr_heap)
        self.assertEqual(expected, arr_heap2)

    def test_sort2(self):
        arr = [30, 1, 5, 7, 3, 29, 8, 5, -3]

        SortMerge = sm.merge_sort(False)
        arr_merge = SortMerge.execute(arr)

        SortBubble = sb.bubble_sort(False)
        arr_bubble = SortBubble.execute(arr)

        SortQuick = sp.quick_sort(False,"random")
        arr_quick = SortQuick.execute(arr)

        SortSelection = ss.selection_sort(False)
        arr_selection = SortSelection.execute(arr)

        SortHeap = sh.heap_sort(False, 100)
        arr_heap = SortHeap.execute(arr)

        SortHeap2 = sh2.heap_sort2(False)
        arr_heap2 = SortHeap2.execute(arr)

        expected = [-3, 1, 3, 5, 5, 7, 8, 29, 30]
        self.assertEqual(expected, arr_merge)
        self.assertEqual(expected, arr_bubble)
        self.assertEqual(expected, arr_quick)
        self.assertEqual(expected, arr_selection)
        self.assertEqual(expected, arr_heap)
        self.assertEqual(expected, arr_heap2)


if __name__ == "__main__":
    unittest.main()
