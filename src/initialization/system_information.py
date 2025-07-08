import sys

def print_python_details() -> None:
    """Prints essential information about the current Python environment.
    
    This function displays key details about the Python interpreter being used,
    including:
    - Python version (major.minor.patch)
    - Python installation path (executable location)
    
    The output is useful for debugging and ensuring the correct Python environment
    is being used, especially in scenarios with multiple Python installations.
    
    Example:
        >>> print_python_details()
        Python Version: 3.9.7
        Installation path: /usr/local/bin/python3.9
    
    Note:
        This function uses sys.version and sys.executable to gather the information.
        No external dependencies are required.
    """
    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Installation path: {sys.executable}\n")