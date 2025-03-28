from colorama import Fore, Back, Style, init
from typing import Any

# Initialize colorama
init(autoreset=True)

class Colors:
    """
    Color configurations for CLI output.
    Provides consistent color formatting across the application.
    
    Usage:
        print(Colors.success("Operation completed"))
        print(f"{Colors.PRIMARY}Processing...{Colors.RESET}")
    """
    # Color constants
    PRIMARY = Fore.CYAN
    SUCCESS = Fore.GREEN
    ERROR = Fore.RED
    WARNING = Fore.YELLOW
    HIGHLIGHT = Fore.MAGENTA
    INFO = Fore.BLUE
    RESET = Style.RESET_ALL
    BOLD = Style.BRIGHT
    
    @staticmethod
    def primary(text: Any) -> str:
        """Format text with primary color"""
        return f"{Colors.PRIMARY}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def success(text: Any) -> str:
        """Format text with success color"""
        return f"{Colors.SUCCESS}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def error(text: Any) -> str:
        """Format text with error color"""
        return f"{Colors.ERROR}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def warning(text: Any) -> str:
        """Format text with warning color"""
        return f"{Colors.WARNING}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def info(text: Any) -> str:
        """Format text with info color"""
        return f"{Colors.INFO}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def highlight(text: Any) -> str:
        """Format text with highlight color"""
        return f"{Colors.HIGHLIGHT}{str(text)}{Colors.RESET}"
    
    @staticmethod
    def bold(text: Any) -> str:
        """Format text with bold style"""
        return f"{Colors.BOLD}{str(text)}{Colors.RESET}"