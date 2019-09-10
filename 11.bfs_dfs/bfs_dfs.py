"""
    Breaadth-first search and depth-first search

    Author By: Lofues
"""

from typing import List, Optional, Generator, IO

class Graph(object):
    """Undirect Graph"""
    def __init__(self,num_vertexs):
        self._num_vertexs = num_vertexs
        self._adjacency = [ [] for _ in range(self._num_vertexs)]

    def add_edge(self, s : int, t: int):
        self._adjacency[s].append(t)
        self._adjacency[t].append(s)

    def _generate_path(self, s : int, t : int, prev : List[Optional[int]]) -> Generator:
        if prev[t] or s != t:
            yield from self._generate_path(s,prev[t],prev)
        yield  str(t)

    def bfs(self, s : int, t : int) -> IO[str]:
        """
        Print out the path from Vertex s to Vertex t using bfs
        """
        if s == t:return

        visited = [False] * self._num_vertexs
        visited[s] = True
        q = [s]
        prev = [None] * self._num_vertexs

        while q:
            v = q.pop(0)
            for neighber in self._adjacency[v]:
                if not visited[neighber]:
                    prev[neighber] = v
                    if neighber == t:
                        print('->'.join(self._generate_path(s,t,prev)))
                        return
                    visited[neighber] = True
                    q.append(neighber)

    def dfs(self, s: int, t: int) -> IO[str]:
        """
            Print out a path from Vertex s to Vertex t using dfs
        """

        found = False
        visited = [False] * self._num_vertexs
        prev = [None] * self._num_vertexs

        def _dfs(from_vertex):
            nonlocal found
            if found:
                return
            visited[from_vertex] = True
            if from_vertex == t:
                found = True
                return
            for neighbor in self._adjacency[from_vertex]:
                if not visited[neighbor]:
                    prev[neighbor] = from_vertex
                    _dfs(neighbor)

        _dfs(s)
        print('->'.join(self._generate_path(s,t,prev)))


if __name__ == "__main__":
    graph = Graph(8)

    graph.add_edge(0, 1)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.add_edge(1, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(4, 6)
    graph.add_edge(5, 7)
    graph.add_edge(6, 7)

    graph.bfs(0, 7)
    graph.dfs(0, 7)
















