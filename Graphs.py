"""
The Graph class represents a directed graph using an adjacency list.
It provides methods to add vertices, add edges, and perform depth-first search (DFS) traversal.
Terminology:
- Graph: A collection of vertices (nodes) and edges (connections between nodes).
- Vertex: A node in the graph.
- Edge: A connection between two vertices.
- Adjacency List: A data structure that represents a graph as a list of lists, where each list contains the vertices adjacent to a given vertex.
- Depth-First Search (DFS): A traversal algorithm that explores as far as possible along each branch before backtracking.
"""

class Graph:
    """
    A class to represent a directed graph using an adjacency list.
    """
    def __init__(self):
        self.graph = {}

    def print_graph(self):
        """
        Prints the graph in a readable format.
        """
        for vertex, edges in self.graph.items():
            print(vertex, ": ", edges)

    def add_vertex(self, vertex):
        """
        Adds a vertex to the graph.
        Args:
            vertex: The vertex to add.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
            return True
        return False

    def add_edge(self, from_vertex, to_vertex):
        """
        Adds a directed edge from one vertex to another.
        Args:
            from_vertex: The starting vertex of the edge.
            to_vertex: The ending vertex of the edge.
        """
        if from_vertex in self.graph and to_vertex in self.graph:
            self.graph[from_vertex].append(to_vertex)
            return True
        return False
    
    def add_bidirectional_edge(self, vertex1, vertex2):
        """
        Adds a bidirectional edge between two vertices.
        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
        """
        if self.add_edge(vertex1, vertex2) and self.add_edge(vertex2, vertex1):
            return True
        return False
    
    def remove_edge(self, from_vertex, to_vertex):
        """
        Removes a directed edge from one vertex to another.
        Args:
            from_vertex: The starting vertex of the edge.
            to_vertex: The ending vertex of the edge.
        """
        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            try:
                self.graph[from_vertex].remove(to_vertex)
            except ValueError:
                pass
            return True
        return False
    
    def remove_bidirectional_edge(self, vertex1, vertex2):
        """
        Removes a bidirectional edge between two vertices.
        Args:
            vertex1: The first vertex of the edge.
            vertex2: The second vertex of the edge.
        """
        if self.remove_edge(vertex1, vertex2) and self.remove_edge(vertex2, vertex1):
            return True
        return False
    
    def remove_vertex(self, vertex):
        """
        Removes a vertex and all its associated edges from the graph.
        Args:
            vertex: The vertex to remove.
        """
        if vertex in self.graph:
            del self.graph[vertex]
            for edges in self.graph.values():
                if vertex in edges:
                    edges.remove(vertex)
            return True
        return False
    
    def remove_vertex_of_bidirectional_graph(self, vertex):
        """
        Removes a vertex and all its associated bidirectional edges from the graph.
        Args:
            vertex: The vertex to remove.
        """
        if vertex in self.graph:
            for v in self.graph[vertex]:
                self.graph[v].remove(vertex)
            del self.graph[vertex]
            return True
        return False

    def dfs(self, start_vertex, visited=None):
        """
        Performs depth-first search (DFS) traversal starting from a given vertex.
        Args:
            start_vertex: The vertex to start the DFS from.
            visited: A set of visited vertices (used for recursion).
        Returns:
            list: A list of vertices in the order they were visited.
        """
        if visited is None:
            visited = set()
        
        visited.add(start_vertex)
        result = [start_vertex]

        for neighbor in self.graph[start_vertex]:
            if neighbor not in visited:
                result.extend(self.dfs(neighbor, visited))
        
        return result
    
if __name__ == "__main__":
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_bidirectional_edge("A", "B")
    g.add_bidirectional_edge("B", "C")
    g.add_bidirectional_edge("A", "C")
    
    print("Graph:")
    g.print_graph()
    
    print("\nRemoving edge A-C:")
    g.remove_bidirectional_edge("A", "C")
    g.print_graph()
    
    print("\nRemoving vertex B:")
    g.remove_vertex("B")
    g.print_graph()
