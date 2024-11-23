import unittest
from sorting_algorithms import quicksort, mergesort, heapsort, insertion_sort, selection_sort, bubble_sort

class TestSortingAlgorithms(unittest.TestCase):
    
    def test_quicksort_happy_path(self):
        self.assertEqual(quicksort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(quicksort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(quicksort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
    
    def test_quicksort_edge_cases(self):
        self.assertEqual(quicksort([]), [])
        self.assertEqual(quicksort([1]), [1])
        self.assertEqual(quicksort([2, 2, 2]), [2, 2, 2])

    def test_mergesort_happy_path(self):
        self.assertEqual(mergesort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(mergesort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(mergesort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
        
    def test_mergesort_edge_cases(self):
        self.assertEqual(mergesort([]), [])
        self.assertEqual(mergesort([1]), [1])
        self.assertEqual(mergesort([2, 2, 2]), [2, 2, 2])
        
    def test_heapsort_happy_path(self):
        self.assertEqual(heapsort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(heapsort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(heapsort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
        
    def test_heapsort_edge_cases(self):
        self.assertEqual(heapsort([]), [])
        self.assertEqual(heapsort([1]), [1])
        self.assertEqual(heapsort([2, 2, 2]), [2, 2, 2])
        
    def test_insertion_sort_happy_path(self):
        self.assertEqual(insertion_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(insertion_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(insertion_sort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
        
    def test_insertion_sort_edge_cases(self):
        self.assertEqual(insertion_sort([]), [])
        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([2, 2, 2]), [2, 2, 2])
        
    def test_selection_sort_happy_path(self):
        self.assertEqual(selection_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(selection_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(selection_sort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
        
    def test_selection_sort_edge_cases(self):
        self.assertEqual(selection_sort([]), [])
        self.assertEqual(selection_sort([1]), [1])
        self.assertEqual(selection_sort([2, 2, 2]), [2, 2, 2])
        
    def test_bubble_sort_happy_path(self):
        self.assertEqual(bubble_sort([3, 2, 1]), [1, 2, 3])
        self.assertEqual(bubble_sort([1, 3, 2]), [1, 2, 3])
        self.assertEqual(bubble_sort([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
        
    def test_bubble_sort_edge_cases(self):
        self.assertEqual(bubble_sort([]), [])
        self.assertEqual(bubble_sort([1]), [1])
        self.assertEqual(bubble_sort([2, 2, 2]), [2, 2, 2])

if __name__ == '__main__':
    unittest.main()
