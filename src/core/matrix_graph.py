from typing import Any, Dict, List, Union, TypeVar, Optional
from exceptions.graph_exceptions import FileReadError, InvalidMatrixError, GraphError

T = TypeVar('T')  # Type variable for degree values
DegreeInfo = Union[int, Dict[str, int]]  # Type alias for degree information

def validate_matrix(matrix: List[List[int]], context: Optional[Dict[str, Any]] = None) -> None:
    """
    Validate adjacency matrix format and values.
    
    Args:
        matrix: The matrix to validate
        context: Additional context for error messages
        
    Raises:
        InvalidMatrixError: If matrix format is invalid
    """
    try:
        if not matrix:
            raise InvalidMatrixError("Matrix cannot be empty")
            
        size = len(matrix)
        for i, row in enumerate(matrix):
            if len(row) != size:
                raise InvalidMatrixError(
                    f"Row {i} has incorrect length ({len(row)} != {size})",
                    size
                )
            if not all(x in (0, 1) for x in row):
                invalid_values = [x for x in row if x not in (0, 1)]
                raise InvalidMatrixError(
                    f"Row {i} contains invalid values: {invalid_values}",
                    size
                )
    except InvalidMatrixError:
        raise
    except Exception as e:
        raise InvalidMatrixError(str(e), context=context)

def load_adjacency_matrix(file_path: str) -> List[List[int]]:
    """
    Load an adjacency matrix from a text file.

    Args:
        file_path: Path to the text file containing the matrix

    Returns:
        List[List[int]]: The loaded adjacency matrix

    Raises:
        FileReadError: If there is an error reading or parsing the file
        InvalidMatrixError: If the matrix format is invalid
    """
    matrix = []
    try:
        with open(file_path, "r") as file:
            for line_num, line in enumerate(file, 1):
                stripped_line = line.strip()
                if not stripped_line:  # Skip empty lines
                    continue
                    
                try:
                    row = [int(x) for x in stripped_line.split()]
                    matrix.append(row)
                except ValueError:
                    raise FileReadError(
                        f"Invalid value in line {line_num}",
                        file_path
                    )
                    
        validate_matrix(matrix)
        return matrix
        
    except FileNotFoundError:
        raise FileReadError("File not found", file_path)
    except Exception as e:
        raise FileReadError(f"Error reading file: {str(e)}", file_path)

def calculate_degrees(matrix: List[List[int]], directed: bool = False) -> Dict[int, DegreeInfo]:
    """Calculate node degrees from adjacency matrix."""
    try:
        context = {"directed": directed}
        validate_matrix(matrix, context)
        
        degrees: Dict[int, DegreeInfo] = {}
        num_nodes = len(matrix)
        
        try:
            if not directed:
                for i in range(num_nodes):
                    degrees[i] = sum(matrix[i])
            else:
                for i in range(num_nodes):
                    out_degree = sum(matrix[i])
                    in_degree = sum(matrix[j][i] for j in range(num_nodes))
                    degrees[i] = {
                        'in_degree': in_degree, 
                        'out_degree': out_degree
                    }
                    
            return degrees
            
        except Exception as e:
            raise InvalidMatrixError(
                "Error calculating degrees",
                matrix_size=num_nodes,
                context={"error": str(e), **context}
            )
            
    except GraphError:
        raise
    except Exception as e:
        raise InvalidMatrixError(f"Unexpected error: {str(e)}")