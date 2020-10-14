"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)   

    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        q = Queue()
        q.enqueue(starting_vertex)
        #mark visited nodes
        visited = set()
        #until queue is empty
        while q.size() > 0:
            vert = q.dequeue() # deQ first node
            if vert not in visited:
                print(vert)
                visited.add(vert)  # mark as visited
                for nextVert in self.get_neighbors(vert):
                    q.enqueue(nextVert)



    def dft(self, starting_vertex):
        s = Stack()
        s.push(starting_vertex)
        visited = set()
        while s.size() > 0:
            vert = s.pop()
            if vert not in visited:
                print(vert)
                visited.add(vert)
                for nextVert in self.get_neighbors(vert):
                    s.push(nextVert)

    def dft_recursive(self, starting_vertex, visited=None):
            if visited is None:
                visited = set()
            if starting_vertex not in visited:
                visited.add(starting_vertex)
                print(starting_vertex)
                for next_vertex in self.get_neighbors(starting_vertex):
                    self.dft_recursive(next_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        q = Queue()
       
        q.enqueue([starting_vertex])
        while q.size() > 0:
           
            path = q.dequeue()
           
            lastVert = path[-1]
       
            if lastVert == destination_vertex:
                return path
            
            for adjacent in self.get_neighbors(lastVert):
                newPath = list(path)
                newPath.append(adjacent)
                q.enqueue(newPath)

    def dfs(self, starting_vertex, destination_vertex):
        path = []
        s = Stack()
        s.push(starting_vertex)

        visited = set()

        while s.size() > 0:
            vert = s.pop()
            if vert not in visited:
                visited.add(vert)
                path.append(vert)
                if vert == destination_vertex:
                    return path

                for nextVert in self.get_neighbors(vert):
                    s.push(nextVert)
        

    def dfs_recursive(self, starting_vertex, destination_vertex,visited=[] ):
        if starting_vertex == destination_vertex:
            print('target found!', starting_vertex)
            return visited + [starting_vertex]
        else:
            visited.append(starting_vertex)
            for edge in self.get_neighbors(starting_vertex):
                print(
                    f'{edge} is a neighbor to {starting_vertex}:{self.get_neighbors(starting_vertex)}')
                if edge not in visited:
                    print(
                        f'{edge} not in visited, recurse, append {starting_vertex} if not in list')
                    path = self.dfs_recursive(
                        edge, destination_vertex, visited)
                    if path:
                        print('path is', path)
                        return path
            visited.remove(starting_vertex)
            print(
                f'Delete: {starting_vertex} its exit {edge} has been visited and no path to {destination_vertex} was found')

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
