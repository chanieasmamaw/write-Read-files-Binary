import unittest
from Unit_Testing import find_min_max  # Importing the find_min_max function from Unit_Testing module

class TestFindMinMax(unittest.TestCase):

    def test_valid_case(self):
        result = find_min_max([1, 2, 5])  # Call the find_min_max function with test input
        self.assertEqual(result, (1, 5), f"Expected (1, 5), but got {result}")
		
    def test_empty_list(self):
         result = find_min_max([])
         self.assertIsNone(result, "Expected Ture for an empty list")
        
    def text_string(self):
        result = find_min_max([ "A" , "B",  "B"])
        self.assertIsNone(result,"The lis must not be string")
        

if __name__ == '__main__':
    unittest.main()

