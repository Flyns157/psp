import sorting_algorithms
import unittest
import inspect
import random

def list_module_functions(module):
    """
    Liste les fonctions définies dans un module.
    
    Args:
        module (module): Le module à analyser.
        
    Returns:
        list: Une liste des noms des fonctions définies dans le module.
    """
    return [name for name, obj in inspect.getmembers(module, inspect.isfunction)]

def gen_random_list(size):
    """
    Génère une liste de taille `size` avec des entiers aléatoires.
    
    Args:
        size (int): La taille de la liste.
        
    Returns:
        list: La liste de taille `size` avec des entiers aléatoires.
    """
    return [random.randint(1, 100) for _ in range(size)]

class TestSortingAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Méthode exécutée une seule fois avant tous les tests.
        """
        cls.module = sorting_algorithms
        cls.functions = list_module_functions(cls.module)

    def test_functions_exist_and_callable(self):
        """
        Vérifie que toutes les fonctions du module existent et sont appelables.
        """
        for func_name in self.functions:
            with self.subTest(func=func_name):
                func = getattr(self.module, func_name)
                self.assertIsNotNone(func)
                self.assertTrue(callable(func))

    def test_sorting_algorithms(self):
        """
        Teste les fonctions de tri avec différents cas de figure.
        """
        test_cases = [
            ([], []),
            ([1], [1]),
            ([2, 1], [1, 2]),
            ([3, 2, 1], [1, 2, 3]),
            ([5, 4, 4, 3, 2], [2, 3, 4, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([1, 3, 2], [1, 2, 3]),
        ]

        for func_name in self.functions:
            func = getattr(self.module, func_name)
            for input_list, expected_output in test_cases:
                with self.subTest(func=func_name, input=input_list):
                    result = func(input_list.copy())
                    self.assertEqual(   result, expected_output, 
                                        msg=f"Function '{func_name}' failed for input {input_list}. Expected {expected_output}, got {result}")

            # Testing with random lists only once for each function to avoid redundancy
            for test_list_size in (50, 100):  # Generate two random tests
                random_test_list = gen_random_list(test_list_size)
                with self.subTest(func=func_name, input=random_test_list):
                    result = func(random_test_list.copy())
                    self.assertEqual(   result, sorted(random_test_list), 
                                        msg=f"Function '{func_name}' failed for random input {random_test_list}. Expected sorted list.")

    def test_invalid_inputs(self):
        """
        Vérifie que les fonctions lèvent des exceptions pour des entrées invalides.
        """
        invalid_inputs = [
            None,
            123,
            "string",
            {1: "one", 2: "two"}
        ]
        for func_name in self.functions:
            func = getattr(self.module, func_name)
            for invalid_input in invalid_inputs:
                with self.subTest(func=func_name, input=invalid_input):
                    with self.assertRaises(TypeError) as context:
                        func(invalid_input)
                    # Ensure the error message is meaningful
                    self.assertIn(  "must be a sequence", str(context.exception),
                                    msg=f"Function '{func_name}' did not raise TypeError for invalid input {invalid_input}.")

if __name__ == '__main__':
    unittest.main()
