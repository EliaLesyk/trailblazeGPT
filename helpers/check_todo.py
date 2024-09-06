import inspect
import re

def check_implementation(obj):
    """
    Check if a function or all methods of a class contain the placeholder 'TODO'.
    
    Args:
    - obj: The function or class to check.

    Raises:
    - NotImplementedError: If 'TODO' is found in any function or method.
    """
    
    # ANSI escape codes for colored output
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
    if inspect.isclass(obj):
        # Check all methods in the class
        methods = inspect.getmembers(obj, predicate=inspect.isfunction)
        todos_found = False
        for method_name, method in methods:
            func_source = inspect.getsource(method)
            # Use a regex to find 'TODO' anywhere in the method's source
            if re.search(r'TODO', func_source, re.IGNORECASE):
                print(f"{RED}'{method_name}' in class '{obj.__name__}' contains a TODO placeholder and must be implemented.{RESET}")
                todos_found = True
        if not todos_found:
            print(f"{GREEN}All methods in class '{obj.__name__}' have been implemented. No TODO found.{RESET}")
    else:
        # Check a standalone function
        func_source = inspect.getsource(obj)
        if 'TODO' in func_source:
            raise NotImplementedError(f"{RED}'{obj.__name__}' contains a TODO placeholder and must be implemented.{RESET}")
        else:
            print(f"{GREEN}'{obj.__name__}' has been implemented. No TODO found.{RESET}")
