# Graph Application: Graph ADT and Adjacency Matrix Operations in Python 🚀

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![Code Style: PEP8](https://img.shields.io/badge/Code%20Style-PEP8-brightgreen)](https://peps.python.org/pep-0008/)

This project implements a graph application in Python that demonstrates two main functionalities:

1. **Graph ADT Operations:**  
   - Create an empty graph  
   - Insert nodes  
   - Insert edges  
   - Check if a graph is empty  
   - Search for a node  

2. **Adjacency Matrix Operations:**  
   - Read an adjacency matrix from a text file  
   - Calculate node degrees for both directed and undirected graphs

The solution is designed with modularity, follows best practices (SOLID, DRY), includes comprehensive error handling, and features an interactive command-line interface.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Folder Structure](#folder-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)
- [Acknowledgements](#acknowledgements)

## 📖 Overview
This project demonstrates the use of graphs as a data structure in Python through two application cases:
- **Graph ADT:** Operations like adding nodes, inserting edges, checking for an empty graph, and searching for nodes are performed interactively by the user.
- **Matrix Graph:** An adjacency matrix is read from a text file to compute the degrees (or in/out degrees for directed graphs) of each node.

The application leverages modular design by separating the graph operations into distinct modules, ensuring clear code organization and ease of maintenance.

## Features
- **Graph ADT Operations:**
  - Create an empty graph (GraphTAD)
  - Insert nodes and edges (with bidirectional option)
  - Check if the graph is empty
  - Search for a node
  - Display the graph's adjacency list

- **Adjacency Matrix Operations:**
  - Load an adjacency matrix from a text file (e.g., `data/matrix.txt`)
  - Calculate node degrees for both undirected and directed graphs
  - Display the loaded matrix and computed degrees

- **Interactive Command-Line Interface:**
  - Separate menus for Graph ADT and Matrix Graph operations
  - Input validation and error handling

- **Modular Design:**
  - Separated modules for Graph ADT (`graph_tad.py`), matrix operations (`matrix_graph.py`), and the main interactive menu (`main.py`)
  - Follows SOLID and DRY principles

## 📂 Folder Structure
A recommended project structure is as follows:
```
└── 📁src
    └── 📁cli
        └── __init__.py
        └── colors.py
        └── menu_base.py
        └── utils.py
    └── 📁core
        └── __init__.py
        └── graph_tad.py
        └── matrix_graph.py
    └── 📁exceptions
        └── __init__.py
        └── graph_exceptions.py
    └── 📁menus
        └── __init__.py
        └── graph_tad_menu.py
        └── matrix_menu.py
    └── __init__.py
    └── config.py
    └── main.py
```
## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Eddy-nio/graph_app.git
   cd graph_app
   ```
2. **Create a virtual environment (optional):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows
   ```
3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application:**
   ```bash
   python src/main.py
   ```
5. **Enjoy!**
   The application should now be running in your terminal.

## 🚀 Usage
The application provides an interactive command-line interface (CLI) for performing various graph operations. The main menu allows you to choose between two types of graphs: Graph ADT and Matrix Graph.
- **Graph ADT:** This menu allows you to create an empty graph, insert nodes and edges, check if the graph is empty, search for a node, and display the graph's adjacency list.
- **Matrix Graph:** This menu allows you to load an adjacency matrix from a text file, calculate node degrees, and display the matrix and degrees.
- **Exit:** This option allows you to exit the application.
> **Note:** The application validates user input and provides error messages for invalid inputs.

## Examples
### Graph ADT Operations
1. **Create an empty graph:**
   - Choose option `1` from the main menu.
   - Enter the number of nodes for the graph (e.g., `5`).
   - The empty graph will be created.
2. **Insert nodes and edges:**
   - Choose option `2` from the main menu.
   - Enter the nodes and edges in the format `node1 node2` (e.g., `1 2`).
   - Repeat the above step for all the edges.
   - The edges will be inserted into the graph.
3. **Check if the graph is empty:**
   - Choose option `3` from the main menu.
   - The application will display whether the graph is empty or not.
4. **Search for a node:**
   - Choose option `4` from the main menu.
   - Enter the node to search for (e.g., `1`).
   - The application will display whether the node is present in the graph or not.
5. **Display the graph's adjacency list:**
   - Choose option `5` from the main menu.
   - The application will display the graph's adjacency list.
6. **Exit the Graph ADT menu:**
   - Choose option `6` from the main menu to exit the Graph ADT menu.

### Matrix Graph Operations
1. **Load an adjacency matrix from a text file:**
   - Choose option `2` from the main menu.
   - Enter the filename of the text file containing the adjacency matrix (e.g., `data/matrix.txt`).
   - The application will load the adjacency matrix from the file.
2. **Calculate node degrees:**
   - Choose option `3` from the main menu.
   - The application will calculate the node degrees (in/out degrees for directed graphs) and display them.
3. **Display the matrix and degrees:**
   - Choose option `4` from the main menu.
   - The application will display the loaded matrix and computed degrees.
4. **Exit the Matrix Graph menu:**
   - Choose option `5` from the main menu to exit the Matrix Graph menu.

## Contributing
Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## Author
Eddy-Nio - [ebecerra@ucompensar.edu.co](mailto:ebecerra@ucompensar.edu.co)

## Acknowledgements
- [Python](https://www.python.org/)
- [Python Packaging User Guide](https://packaging.python.org/)
- [Click](https://click.palletsprojects.com/)
- [Rich](https://rich.readthedocs.io/)
- [Pytest](https://pytest.org/)
- Data Structures course at Universidad Compensar
- Python community for excellent documentation
