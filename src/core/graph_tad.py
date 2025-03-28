from typing import TypeVar, Dict, List, Optional, Any, Set
from exceptions.graph_exceptions import NodeError, EdgeError

T = TypeVar('T')  # Type variable for node values

class GraphTAD:
    """
    A Graph Abstract Data Type (ADT) implemented using an adjacency list.
    
    Attributes:
        adj_list: Dictionary mapping nodes to their adjacent nodes
    
    Methods:
        is_empty: Check if the graph is empty
        add_node: Insert a node into the graph
        add_edge: Insert an edge between nodes
        remove_node: Remove a node and its edges
        search_node: Check if a node exists
        get_neighbors: Get adjacent nodes
        get_degree: Get node degree
    """

    MAX_RETRIES = 3  # Maximum number of retries for operations

    def __init__(self) -> None:
        """Initialize an empty graph."""
        self.adj_list: Dict[T, List[T]] = {}

    def _validate_node(self, node: T, check_exists: bool = False, context: Optional[Dict[str, Any]] = None) -> None:
        """
        Validates a node to ensure it meets the required conditions.
        This method checks if the provided node is valid based on the specified criteria.
        It raises appropriate exceptions if the validation fails.
            node (T): The node to validate.
            check_exists (bool, optional): If True, checks whether the node exists in the adjacency list. 
                Defaults to False.
            context (Optional[Dict[str, Any]], optional): Additional context information to include in 
                error messages. Defaults to None.
            NodeError: If the node is None, has an empty ID, or does not exist (when `check_exists` is True).
            NodeError: If an unexpected error occurs during validation.
        """
        try:
            if node is None:
                raise NodeError("Node cannot be None", context=context)
            if not str(node).strip():
                raise NodeError("Node ID cannot be empty", context=context)
            if check_exists and node not in self.adj_list:
                raise NodeError(
                    "Node does not exist",
                    str(node),
                    context or {"available_nodes": list(self.adj_list.keys())}
                )
        except NodeError:
            raise
        except Exception as e:
            raise NodeError(f"Unexpected error validating node: {str(e)}", str(node), context)

    def is_empty(self) -> bool:
        """Check if the graph is empty."""
        return len(self.adj_list) == 0

    def add_node(self, node: T) -> None:
        """Add node with retry mechanism."""
        retries = 0
        last_error = None
        
        while retries < self.MAX_RETRIES:
            try:
                context = {"attempt": retries + 1, "max_retries": self.MAX_RETRIES}
                self._validate_node(node, context=context)
                
                if node in self.adj_list:
                    raise NodeError(
                        "Node already exists",
                        str(node),
                        context={"existing_nodes": list(self.adj_list.keys())}
                    )
                    
                self.adj_list[node] = []
                return
                
            except NodeError as e:
                last_error = e
                retries += 1
                
        if last_error:
            raise NodeError(
                f"Failed to add node after {self.MAX_RETRIES} attempts",
                str(node),
                context={"last_error": str(last_error)}
            )

    def add_edge(self, from_node: T, to_node: T, bidirectional: bool = True) -> None:
        """Add edge with enhanced validation."""
        context = {
            "bidirectional": bidirectional,
            "existing_nodes": list(self.adj_list.keys())
        }
        
        try:
            self._validate_node(from_node, context=context)
            self._validate_node(to_node, context=context)
            
            if from_node == to_node:
                raise EdgeError(
                    "Self loops are not allowed",
                    str(from_node),
                    str(to_node),
                    bidirectional
                )

            # Add nodes if they don't exist
            for node in (from_node, to_node):
                if node not in self.adj_list:
                    self.add_node(node)

            # Add edge(s)
            if to_node not in self.adj_list[from_node]:
                self.adj_list[from_node].append(to_node)
            if bidirectional and from_node not in self.adj_list[to_node]:
                self.adj_list[to_node].append(from_node)
                
        except (NodeError, EdgeError):
            raise
        except Exception as e:
            raise EdgeError(
                f"Unexpected error adding edge: {str(e)}",
                str(from_node),
                str(to_node),
                bidirectional
            )

    def remove_node(self, node: T) -> None:
        """Remove a node and all its edges from the graph."""
        self._validate_node(node, check_exists=True)

        # Remove edges pointing to this node
        for other_node in self.adj_list:
            if node in self.adj_list[other_node]:
                self.adj_list[other_node].remove(node)

        # Remove the node
        del self.adj_list[node]

    def get_nodes(self) -> Set[T]:
        """
        Get all nodes in the graph.
        
        Returns:
            Set[T]: Set of all nodes
        """
        return set(self.adj_list.keys())

    def get_neighbors(self, node: T) -> List[T]:
        """
        Get all neighbors of a node.
        
        Args:
            node: Node to get neighbors for
            
        Returns:
            List[T]: List of neighboring nodes
            
        Raises:
            NodeError: If node does not exist
        """
        self._validate_node(node, check_exists=True)
        return self.adj_list[node].copy()  # Return copy to prevent modification

    def get_degree(self, node: T) -> int:
        """Get the degree of a node."""
        self._validate_node(node, check_exists=True)
        return len(self.adj_list[node])

    def search_node(self, node: T) -> bool:
        """Check if a node exists in the graph."""
        try:
            self._validate_node(node)
            return node in self.adj_list
        except NodeError:
            return False

    def __str__(self) -> str:
        """Get string representation of the graph."""
        if self.is_empty():
            return "Empty graph"
        
        result = []
        for node, neighbors in self.adj_list.items():
            neighbors_str = ", ".join(map(str, neighbors)) if neighbors else "∅"
            result.append(f"{node} → [{neighbors_str}]")
        return "\n".join(result)
