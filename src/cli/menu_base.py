from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Optional, List
import os

from exceptions.graph_exceptions import InvalidChoiceError
from .colors import Colors

T = TypeVar('T')

class MenuBase(ABC, Generic[T]):
    """Enhanced abstract base class for menus"""
    
    def __init__(self, title: str):
        self.title = title
        self._options: Dict[int, str] = {}
        self._handlers: Dict[int, callable] = {}

    def clear_screen(self) -> None:
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_header(self) -> None:
        """Display formatted header with centered title"""
        self.clear_screen()
        width = max(len(self.title) + 8, 40)  # Minimum width of 40 chars
        border = "=" * width
        padding = " " * ((width - len(self.title)) // 2)
        
        print(f"\n{Colors.bold(border)}")
        print(f"{Colors.bold('|')}{padding}{Colors.primary(self.title)}{padding}{Colors.bold('|')}")
        print(f"{Colors.bold(border)}\n")

    def display_menu_option(self, key: str, description: str) -> None:
        """Display formatted menu option with consistent spacing"""
        print(f"  {Colors.info(f'[{key}]')} {description}")

    def display_error(self, message: str) -> None:
        """Display formatted error message"""
        print(f"\n  {Colors.error(f'✗ Error: {message}')}")

    def display_success(self, message: str) -> None:
        """Display formatted success message"""
        print(f"\n  {Colors.success(f'✓ {message}')}")

    def get_input(self, prompt: str, valid_choices: Optional[List[str]] = None) -> str:
        """Get validated user input"""
        while True:
            value = input(f"  {Colors.primary(prompt)}: ").strip()
            if not value:
                self.display_error("Input cannot be empty")
                continue
            if valid_choices and value not in valid_choices:
                self.display_error(f"Please enter one of: {', '.join(valid_choices)}")
                continue
            return value

    def add_option(self, key: int, description: str, handler: callable) -> None:
        """Register a menu option with input validation"""
        if key in self._options:
            raise ValueError(f"Option key {key} already exists")
        if not callable(handler):
            raise ValueError("Handler must be callable")
        
        self._options[key] = description
        self._handlers[key] = handler

    def _handle_choice(self, choice: int) -> None:
        """Execute the handler for the selected option with error handling"""
        handler = self._handlers.get(choice)
        if not handler:
            raise InvalidChoiceError(
                "Invalid menu choice",
                choice=choice,
                valid_choices=list(self._options.keys())
            )
        
        try:
            handler()
        except Exception as e:
            self.display_error(str(e))

    def pause(self, message: str = "Press Enter to continue...") -> None:
        """Pause execution until user input"""
        input(f"\n  {Colors.info(message)}")

    @abstractmethod
    def run(self) -> None:
        """Execute menu logic"""
        pass