from cli.menu_base import MenuBase
from cli.colors import Colors
from core.matrix_graph import load_adjacency_matrix, calculate_degrees
from exceptions.graph_exceptions import GraphError, FileReadError, InvalidMatrixError
import os
from typing import Optional, List, Dict

class MatrixMenu(MenuBase[None]):
    """Menu for Matrix Graph operations"""
    def __init__(self):
        super().__init__("Matrix Graph Operations")
        self.current_matrix: Optional[List[List[int]]] = None
        self._setup_options()

    def run(self) -> None:
        """Execute matrix menu loop"""
        while True:
            try:
                self.display_header()
                # Display menu options using parent class method
                for key, description in self._options.items():
                    self.display_menu_option(str(key), description)
                
                choice = int(self.get_input("Enter choice", [str(i) for i in range(1, 5)]))
                if choice == 4:
                    break
                    
                self._handle_choice(choice)
                
            except GraphError as e:
                self.display_error(str(e))
            except Exception as e:
                self.display_error(f"Unexpected error: {str(e)}")
            
            self.pause()

    def _setup_options(self) -> None:
        """Initialize menu options"""
        self.add_option(1, "Load Matrix from File", self._load_matrix)
        self.add_option(2, "Display Current Matrix", self._display_matrix)
        self.add_option(3, "Calculate Degrees", self._calculate_degrees)
        self.add_option(4, "Return to Main Menu", lambda: None)

    def _load_matrix(self) -> None:
        """Load matrix from file with retry mechanism"""
        retries = 0
        while retries < 3:  # Maximum 3 retries
            try:
                # Get file path
                file_path = self.get_input("Enter matrix file path")
                if not file_path.strip():
                    self.display_error("File path cannot be empty")
                    continue

                if not os.path.exists(file_path):
                    self.display_error(f"File not found: {file_path}")
                    continue

                # Load matrix
                self.current_matrix = load_adjacency_matrix(file_path)
                self.display_success("Matrix loaded successfully")
                return

            except (FileReadError, InvalidMatrixError) as e:
                self.display_error(str(e))
                if retries < 2:  # Don't ask on last retry
                    if not self.get_input("Try again? (y/n)", ["y", "n"]).lower() == "y":
                        break
            except Exception as e:
                self.display_error(f"Unexpected error: {str(e)}")
                break
                
            retries += 1
        
        if retries == 3:
            self.display_error("Maximum retries reached")

    def _display_matrix(self) -> None:
        """Display current matrix if loaded"""
        if not self.current_matrix:
            self.display_error("No matrix loaded")
            return

        print("\nCurrent Matrix:")
        for i, row in enumerate(self.current_matrix):
            print(f"  {Colors.info(f'[{i}]')} {' '.join(str(x) for x in row)}")

    def _calculate_degrees(self) -> None:
        """Calculate and display node degrees"""
        if not self.current_matrix:
            self.display_error("No matrix loaded")
            return

        try:
            # Get graph type
            directed = self.get_input("Is this a directed graph? (y/n)", ["y", "n"]).lower() == "y"
            
            # Calculate degrees
            degrees = calculate_degrees(self.current_matrix, directed)
            
            # Display results
            print("\nDegree Calculations:")
            for node, degree in degrees.items():
                if directed:
                    print(f"  Node {node}: In={degree['in_degree']}, Out={degree['out_degree']}")
                else:
                    print(f"  Node {node}: Degree={degree}")
                    
        except GraphError as e:
            self.display_error(str(e))