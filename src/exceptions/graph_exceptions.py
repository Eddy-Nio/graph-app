from typing import Optional, Any, List, Dict
from enum import Enum, auto

class ErrorCode(Enum):
    """Error codes for graph operations"""
    INVALID_NODE = auto()
    INVALID_EDGE = auto()
    INVALID_MATRIX = auto()
    FILE_ERROR = auto()
    MENU_ERROR = auto()
    INVALID_CHOICE = auto()

class GraphError(Exception):
    """Base exception for graph operations"""
    def __init__(self, message: str, details: Optional[str] = None, code: ErrorCode = None):
        self.message = message
        self.details = details
        self.code = code
        super().__init__(self.message)
    
    def __str__(self) -> str:
        """String representation of the error"""
        error_str = self.message
        if self.details:
            error_str += f" ({self.details})"
        if self.code:
            error_str = f"[{self.code.name}] {error_str}"
        return error_str

class InvalidMatrixError(GraphError):
    """Raised when matrix validation fails"""
    def __init__(self, message: str, matrix_size: Optional[int] = None):
        details = f"Matrix size: {matrix_size}" if matrix_size else None
        super().__init__(message, details, ErrorCode.INVALID_MATRIX)

class FileReadError(GraphError):
    """Raised when file operations fail"""
    def __init__(self, message: str, filename: Optional[str] = None, line_number: Optional[int] = None):
        details = f"File: {filename}"
        if line_number is not None:
            details += f", Line: {line_number}"
        super().__init__(message, details, ErrorCode.FILE_ERROR)

class NodeError(GraphError):
    """Raised when node operations fail"""
    def __init__(self, message: str, node_id: Optional[str] = None, context: Optional[Dict[str, Any]] = None):
        details = f"Node: {node_id}"
        if context:
            details += f", Context: {context}"
        super().__init__(message, details, ErrorCode.INVALID_NODE)

class EdgeError(GraphError):
    """Raised when edge operations fail"""
    def __init__(self, 
                 message: str, 
                 from_node: Optional[str] = None, 
                 to_node: Optional[str] = None,
                 bidirectional: bool = False):
        details = f"Edge: {from_node} -> {to_node}"
        if bidirectional:
            details += " (bidirectional)"
        super().__init__(message, details, ErrorCode.INVALID_EDGE)

class MenuError(GraphError):
    """Raised when menu operations fail"""
    def __init__(self, message: str, details: Optional[str] = None):
        super().__init__(message, details, ErrorCode.MENU_ERROR)

class InvalidChoiceError(MenuError):
    """Raised when user provides invalid menu choice"""
    def __init__(self, 
                 message: str, 
                 choice: Any = None, 
                 valid_choices: Optional[List[Any]] = None,
                 retry_count: Optional[int] = None):
        details = f"Choice: {choice}"
        if valid_choices:
            details += f", Valid choices: {valid_choices}"
        if retry_count is not None:
            details += f", Attempts: {retry_count}"
        super().__init__(message, details)
        self.choice = choice
        self.valid_choices = valid_choices