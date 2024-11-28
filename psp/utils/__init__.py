from types import ModuleType
import inspect
import random

from .type_checker import type_check

Array = list[int | float]

def get_classes_from_module(module):
    """
    Retrieve a list of all class names defined in a given Python module.

    Args:
        module (ModuleType): The Python module to inspect.

    Returns:
        list: A list of classes defined in the module.
    """
    if not isinstance(module, ModuleType):
        raise TypeError(f"Expected a module, got {type(module).__name__}")

    # Retrieve classes defined in the module
    return [ member
                for name, member in inspect.getmembers(module, inspect.isclass)
                if member.__module__ == module.__name__]

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

@type_check
def validate_array(arr: Array, min_size: int | float = 0, max_size: int | float = float('inf')) -> bool:
    """
    Vérifie si la liste `arr` est bien une liste d'entiers ou de flottants et de taille suffisante (2 <= len(arr)).
    
    Args:
        arr (list): La liste à vérifier.
        
    Returns:
        bool: True si la liste est valide, False sinon.
    """
    return min_size <= len(arr) <= max_size
