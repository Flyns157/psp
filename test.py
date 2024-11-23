import sorting_algorithms
import unittest
import inspect

def list_module_functions(module):
    return [name for name, obj in inspect.getmembers(module, inspect.isfunction)]

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.module = sorting_algorithms
        self.functions = list_module_functions(self.module)
        for func in self.functions:
            setattr(self, f"test_{func}_happy", self.create_test_function(func))

    def create_test_function(self, func_name):
        def test_function(self):
            func = getattr(self.module, func_name)
            self.assertIsNotNone(func)
            self.assertTrue(callable(func))
            
            with self.assertRaises(TypeError):
                func()
            
            with self.assertRaises(TypeError):
                func(1, 2, 3)
            
            with self.assertRaises(TypeError):
                func("abc")
            
            with self.assertRaises(TypeError):
                func([1, 2, 3])

            # Replace this with valid expected results based on function behavior
            self.assertEqual(func([]), [])
            self.assertEqual(func([1]), [1])
            self.assertEqual(func([1, 2]), [1, 2])
            self.assertEqual(func([2, 1]), [1, 2])
            self.assertEqual(func([3, 2, 1]), [1, 2, 3])
            self.assertEqual(func([1, 3, 2]), [1, 2, 3])
            self.assertEqual(func([5, 4, 4, 3, 2]), [2, 3, 4, 4, 5])
            self.assertEqual(func([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        return test_function

if __name__ == '__main__':
    unittest.main()
