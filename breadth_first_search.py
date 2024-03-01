"""
Implementing breadth first search algorithm
"""
from typing import List, Dict, Set, Optional
# Set ex: set1 = {1, 2, 3, 4, 5}
# Optional is used to indicate that a variable might be None
from collections import deque 

class Graph:
    def __init__(self, graph_dict: Optional[Dict[str, List[str]]] = None):
        if graph_dict is None:
            graph_dict = {} # empty dictionary
        self.__graph_dict = graph_dict # private attribute, can only be accessed within the class
    
    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge: tuple) -> None: # edge is a tuple of two vertices
        (vertex1, vertex2) = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2] 
    
    def get_vertices(self) -> List[str]:
        return list(self.__graph_dict.keys())
    
    def get_edges(self) -> List[tuple]:
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.append((vertex, neighbour))
        
        return edges
    
    def __str__(self) -> str: # overload the str() function to print the graph
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.get_edges():
            res += str(edge) + " "
        
        return res
    
    def __getitem__(self, vertex: str) -> List[str]: # overload the [] operator to get the value of a vertex
        return self.__graph_dict[vertex]
    
    def __iter__(self): # overload the iter() function to iterate through the graph
        return iter(self.__graph_dict)
    
    def __len__(self) -> int:
        return len(self.__graph_dict)
    
    def __contains__(self, vertex: str) -> bool:
        return vertex in self.__graph_dict
    
    def __repr__(self) -> str:
        return str(self.__graph_dict)
    

def breadth_first_search(graph: Graph, start: str) -> List[str]:
    if start not in graph:
        raise ValueError(f"{start} is not in the graph")
    
    visited: Set[str] = set() # It means that visited is a set of strings
    queue = deque() # It means that queue is a deque
    queue.append(start)
    visited.add(start)
    while queue: # while queue is not empty
        vertex = queue.popleft() # dequeue a vertex from the queue and assign it to vertex
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    
    return list(visited)


def breadth_first_search_path(graph: Graph, start: str, goal: str) -> Optional[List[str]]:
    if start not in graph:
        raise ValueError(f"{start} is not in the graph")
    
    visited: Set[str] = set()
    queue = deque()
    queue.append(start)
    visited.add(start) # visited is a set!
    parent = {start: None} # using parent to store the path, put it none for the start vertex
    while queue:
        vertex = queue.popleft()
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1] # reverse the path, ex [1, 2, 3] -> [3, 2, 1] in order to get the correct path
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                parent[neighbour] = vertex
    
    return None


if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_vertex("H")
    graph.add_edge(("A", "B"))
    graph.add_edge(("A", "C"))
    graph.add_edge(("A", "D"))
    graph.add_edge(("B", "E"))
    graph.add_edge(("B", "F"))
    graph.add_edge(("C", "G"))
    graph.add_edge(("C", "H"))
    graph.add_edge(("D", "H"))
    graph.add_edge(("E", "F"))
    graph.add_edge(("G", "H"))
    print(graph) # is equivalent to print(graph.__str__())
    print(breadth_first_search(graph, "A"))
    print(breadth_first_search_path(graph, "A", "H"))
    print(breadth_first_search_path(graph, "A", "Z"))