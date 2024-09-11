import unittest
import hw2_debugging

class test_cases(unittest.TestCase):
    def test_correctlySorted(self):
        arr = [1,5,4,3,2]
        correct = [1,2,3,4,5]
        self.assertEqual(merge_sort(arr),correct)
    
