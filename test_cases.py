import unittest
import hw2_debugging
from hw2_debugging import merge_sort

class test_cases(unittest.TestCase):
    def test_correctly_sorted(self):
        arr = [1,5,4,3,2]
        correct = [1,2,3,4,5]
        self.assertEqual(merge_sort(arr),correct)

    def test_jumbled_Order_or_Correct_order(self):
        arr = [1,2,3,4,5]
        expected = [1,2,3,4,5]
        self.assertEqual(merge_sort(arr),expected)

    def check_sorting_negative_numbers(self):
        arr = [-5,-6,-1,-2,-3,-4]
        expected = [-6,-5,-4,-3,-2,-1]
        self.assertEqual(merge_sort(arr),expected)

        
    
