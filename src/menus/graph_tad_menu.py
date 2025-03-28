from cli.menu_base import MenuBase
from core.graph_tad import GraphTAD
from exceptions.graph_exceptions import GraphError

class GraphTADMenu(MenuBase[None]):
    """Menu for Graph TAD operations"""
    def __init__(self):
        super().__init__("Graph TAD Operations")
        self.graph = GraphTAD()
        self._setup_options()

    def _setup_options(self) -> None:
        """Initialize menu options and handlers"""
        self.add_option(1, "Add Node", self._add_node)
        self.add_option(2, "Add Edge", self._add_edge)
        self.add_option(3, "Remove Node", self._remove_node)
        self.add_option(4, "Display Graph", self._display_graph)
        self.add_option(5, "Search Node", self._search_node)
        self.add_option(6, "Return to Main Menu", lambda: None)

    def run(self) -> None:
        """Execute Graph TAD menu loop"""
        while True:
            try:
                self.display_header()
                # Display menu options using parent class method
                for key, description in self._options.items():
                    self.display_menu_option(str(key), description)
                
                choice = int(self.get_input("Enter choice", 
                                          [str(i) for i in range(1, 7)]))
                if choice == 6:
                    self.display_success("Returning to main menu")
                    break
                    
                self._handle_choice(choice)
                
            except GraphError as e:
                self.display_error(str(e))
            except Exception as e:
                self.display_error(f"Unexpected error: {str(e)}")
            
            self.pause()

    def _add_node(self) -> None:
        """Handle node addition"""
        node = self.get_input("Enter node value")
        self.graph.add_node(node)
        self.display_success(f"Node '{node}' added successfully")

    def _add_edge(self) -> None:
        """Handle edge addition"""
        if self.graph.is_empty():
            raise GraphError("Cannot add edge to empty graph")
            
        nodes = self.graph.get_nodes()
        print(f"\n  Current nodes: {nodes}")
        
        from_node = self.get_input("Enter source node", nodes)
        to_node = self.get_input("Enter destination node", nodes)
        is_bidirectional = self.get_input("Make bidirectional? (y/n)", ["y", "n"]) == "y"
        
        self.graph.add_edge(from_node, to_node, is_bidirectional)
        self.display_success("Edge added successfully")

    def _remove_node(self) -> None:
        """Handle node removal"""
        if self.graph.is_empty():
            raise GraphError("Graph is empty")
            
        nodes = self.graph.get_nodes()
        print(f"\n  Current nodes: {nodes}")
        node = self.get_input("Enter node to remove", nodes)
        
        self.graph.remove_node(node)
        self.display_success(f"Node '{node}' removed successfully")

    def _display_graph(self) -> None:
        """Display current graph state"""
        if self.graph.is_empty():
            print("\n  Graph is empty")
            return
            
        print("\n  Current Graph Structure:")
        print(self.graph)

    def _search_node(self) -> None:
        """Handle node search"""
        if self.graph.is_empty():
            raise GraphError("Graph is empty")
            
        node = self.get_input("Enter node to search")
        
        if self.graph.search_node(node):
            self.display_success(f"Node '{node}' found in graph")
        else:
            self.display_error(f"Node '{node}' not found in graph")