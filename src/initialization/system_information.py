import sys

def print_python_details() -> None:
    """_summary_

    Args:
        detailed (bool, optional): _description_. Defaults to False.

    Raises:
        ParametersError: _description_
    """    

    print(f"Python Version: {sys.version.split()[0]}")
    print(f"Installation path: {sys.executable}\n")