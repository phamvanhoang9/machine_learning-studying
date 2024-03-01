"""
Depth first search algorithm:
- Start from the initial vertex and go as deep as possible along each branch before backtracking
- Use a stack to keep track of the vertices to visit
- Use a set to keep track of the visited vertices
- Time complexity: O(V + E), where V is the number of vertices and E is the number of edges
- Space complexity: O(V), where V is the number of vertices
"""

from typing import List, Tuple, Set, Optional

# Define a graph class
class Graph:
    def __init__(self) -> None:
        self.__graph_dict = {}
    
    def add_vertex(self, vertex: str) -> None:
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []
    
    def add_edge(self, edge: Tuple[str, str]) -> None:
        vertex1, vertex2 = edge
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def get_vertices(self) -> List[str]:
        return list(self.__graph_dict.keys())
    
    def get_edges(self) -> List[Tuple[str, str]]:
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
    
# Define a depth first search function
def depth_first_search(graph: Graph, start: str) -> List[str]:
    if start not in graph:
        raise ValueError(f"{start} is not in the graph")
    
    visited: Set[str] = set()
    stack: List[str] = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend([neighbour for neighbour in graph[vertex] if neighbour not in visited])
    
    return list(visited)

def depth_first_search_recursive(graph: Graph, start: str, visited: Optional[Set[str]] = None) -> List[str]:
    if start not in graph:
        raise ValueError(f"{start} is not in the graph")
    
    if visited is None:
        visited = set()
    visited.add(start)
    for neighbour in graph[start]:
        if neighbour not in visited:
            depth_first_search_recursive(graph, neighbour, visited)
    
    return list(visited)

def depth_first_search_path(graph: Graph, start: str, goal: str)-> Optional[List[str]]:
    if start not in graph:
        raise ValueError(f"{start} is not in the graph")
    
    visited: Set[str] = set()
    stack: List[str] = [start]
    parent: dict[str, Optional[str]] = {start: None}
    while stack:
        vertex = stack.pop()
        if vertex == goal:
            path = []
            while vertex is not None:
                path.append(vertex)
                vertex = parent[vertex]
            return path[::-1]
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                stack.append(neighbour)
                parent[neighbour] = vertex
    
    return None


# Test the depth first search function
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("F")
    graph.add_vertex("G")
    graph.add_edge(("A", "B"))
    graph.add_edge(("A", "C"))
    graph.add_edge(("B", "D"))
    graph.add_edge(("B", "E"))
    graph.add_edge(("C", "F"))
    graph.add_edge(("C", "G"))
    # print(graph)
    # print(depth_first_search(graph, "A")) # ['A', 'C', 'G', 'F', 'B', 'E', 'D']
    # print(depth_first_search_recursive(graph, "A")) 
    print(depth_first_search_path(graph, "A", "G")) # ['A', 'C', 'G']
    print(depth_first_search_path(graph, "A", "E")) # ['A', 'B', 'E']
