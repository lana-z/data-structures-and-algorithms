class Graph:
    """
    docstring

    """

    def __init__(self):
        """
        docstring
        """

        self.adjacency_list = {}


#vertices and nodes are the same thing

    def add_node(self, value):
        """
        adds a new node (i.e. vertex) to the graph
        the value parameter is the value of the new node
        return the instance of the new node/vertex
        """

        vertex = Vertex(value)
        self.adjacency_list[vertex] = []
        return vertex

    def size(self):
        """
        returns the total number of nodes in the graph
        """
        return len(self.adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=None):
        """
        adds a new edge between two nodes in the graph
        """
        if start_vertex not in self.adjacency_list or end_vertex not in self.adjacency_list:
            raise KeyError("Start or end vertex not in graph.")

        edge = Edge(end_vertex, weight)
        self.adjacency_list[start_vertex].append(edge)

    def __repr__(self):
        return f"Graph({self.adjacency_list})"

    def get_neighbors(self, vertex):
        """
        returns a collection of edges connected to the given node
        """
        pass

    def get_nodes(self):
        """
        returns all of the nodes in the graph as a collection
        """
        pass

class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self) -> str:
        return f"Vertext(\"{self.value}\")"

class Edge:
    def __init__(self, vertex, weight=None):
        self.vertex = vertex
        self.weight = weight

    def __repr__(self) -> str:
        return f"Edge({self.vertex}, {self.weight})"


