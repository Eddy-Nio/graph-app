from typing import Callable, TypeVar, Any

from src.cli.colors import Colors
from src.exceptions.graph_exceptions import InvalidChoiceError

T = TypeVar('T')

def validate_input(
    prompt: str,
    validator: Callable[[str], T],
    error_msg: str = "Invalid input",
    retries: int = 3
) -> T:
    """Generic input validation with retry logic"""
    attempts = 0
    while attempts < retries:
        try:
            user_input = input(f"{Colors.PRIMARY}{prompt}: {Colors.RESET}")
            return validator(user_input)
        except ValueError:
            attempts += 1
            remaining = retries - attempts
            if remaining > 0:
                print(f"{Colors.WARNING}{error_msg}. {remaining} attempts remaining{Colors.RESET}")
            else:
                raise InvalidChoiceError(error_msg)