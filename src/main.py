#!/usr/bin/env python3
"""
Graph Application - Main entry point
Uses colorama for enhanced CLI and follows SOLID principles with modular design
"""

import logging
from typing import Dict, Optional
import sys

from cli.colors import Colors
from cli.menu_base import MenuBase
from menus.graph_tad_menu import GraphTADMenu
from menus.matrix_menu import MatrixMenu
from exceptions.graph_exceptions import GraphError, InvalidChoiceError, MenuError
from config import AppConfig

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MainMenu(MenuBase[None]):
    """Main application menu implementation"""
    def __init__(self, config: Optional[AppConfig] = None):
        super().__init__("Graph Application")
        self.config = config or AppConfig()
        if self.config.DEBUG:
            logger.setLevel(logging.DEBUG)
            
        self.menus: Dict[int, MenuBase] = {}
        self._initialize_menus()
        self._setup_options()

    def run(self) -> None:
        """Execute main menu loop"""
        while True:
            try:
                self.display_header()
                self._display_options()
                
                # Get and validate user choice
                choice = int(self.get_input("Enter choice", 
                                          [str(i) for i in range(1, 4)]))
                
                # Handle exit option
                if choice == 3:
                    self.display_success("Goodbye!")
                    self._exit_program()
                    break
                
                # Handle menu choice
                self._handle_choice(choice)
                
            except KeyboardInterrupt:
                logger.warning("Program interrupted by user")
                self.display_error("Program interrupted by user")
                break
            except ValueError:
                self.display_error("Please enter a valid number")
            except InvalidChoiceError as e:
                self.display_error(str(e))
            except MenuError as e:
                self.display_error(str(e))
            except Exception as e:
                logger.error(f"Unexpected error: {e}", exc_info=True)
                self.display_error(f"An unexpected error occurred: {str(e)}")
                if self.config.DEBUG:
                    raise
            
            self.pause()

    def _display_options(self) -> None:
        """Display available menu options"""
        for key, description in self._options.items():
            self.display_menu_option(str(key), description)

    def _initialize_menus(self) -> None:
        """Initialize submenu instances"""
        try:
            self.menus = {
                1: GraphTADMenu(),
                2: MatrixMenu()
            }
            logger.debug("Menus initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize menus: {e}")
            raise MenuError("Failed to initialize application menus")

    def _setup_options(self) -> None:
        """Initialize menu options and handlers"""
        try:
            self.add_option(1, "Graph TAD Operations", lambda: self._run_submenu(1))
            self.add_option(2, "Matrix Graph Operations", lambda: self._run_submenu(2))
            self.add_option(3, "Exit", self._exit_program)
            logger.debug("Menu options set up successfully")
        except Exception as e:
            logger.error(f"Failed to setup menu options: {e}")
            raise MenuError("Failed to setup menu options")

    def _run_submenu(self, choice: int) -> None:
        """Execute selected submenu with error handling"""
        menu = self.menus.get(choice)
        if not menu:
            logger.error(f"Invalid menu choice: {choice}")
            raise MenuError(f"Invalid menu selection: {choice}")
            
        try:
            logger.debug(f"Running submenu {choice}")
            menu.run()
        except GraphError as e:
            logger.error(f"Graph operation error: {e}")
            self._handle_graph_error(e)
        except Exception as e:
            logger.error(f"Unexpected error in submenu: {e}")
            self.display_error(f"Unexpected error: {str(e)}")

    def _handle_graph_error(self, error: GraphError) -> None:
        """Format and display graph operation errors"""
        error_msg = str(error)
        if error.details:
            error_msg += f" ({error.details})"
        logger.error(f"Graph error: {error_msg}")
        print(f"\n{Colors.ERROR}Graph operation error: {error_msg}{Colors.RESET}")

    def _exit_program(self) -> None:
        """Clean exit from the program"""
        logger.info("Application shutting down")
        print(f"\n{Colors.SUCCESS}Goodbye!{Colors.RESET}")
        sys.exit(0)

def check_dependencies() -> None:
    """Verify required dependencies and configurations"""
    try:
        # Add any startup checks here
        logger.debug("Dependencies checked successfully")
    except Exception as e:
        logger.critical(f"Dependency check failed: {e}")
        print(f"{Colors.ERROR}Failed to initialize application: {e}{Colors.RESET}")
        sys.exit(1)

def main() -> None:
    """Application entry point"""
    try:
        # Initialize configuration
        config = AppConfig()
        
        # Perform startup checks
        check_dependencies()
        
        # Run main menu
        logger.info("Starting application")
        menu = MainMenu(config)
        menu.run()
        
    except KeyboardInterrupt:
        logger.warning("Program terminated by user")
        print(f"\n\n{Colors.WARNING}Program terminated by user{Colors.RESET}")
    except Exception as e:
        logger.critical(f"Fatal error: {e}", exc_info=True)
        print(f"\n{Colors.ERROR}Fatal error: {str(e)}{Colors.RESET}")
        if config.DEBUG:
            raise
        sys.exit(1)

if __name__ == '__main__':
    main()