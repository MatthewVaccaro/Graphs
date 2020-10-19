test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]


class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:
    def __init__(self):
        # adj list (dictionary) of vertices mapping labels to edges
        self.verts = {}

    def add_vertex(self, vertex_id):
        if vertex_id not in self.verts:
            self.verts[vertex_id] = set()

    def add_edge(self, v1, v2):
        if v1 in self.verts and v2 in self.verts:
            self.verts[v1].add(v2)

def earliest_ancestor(ancestors, starting_node):
     # build graph to traverse
    g = Graph()
    # populate w verts
    for i in ancestors:
        g.add_vertex(i[0])
        g.add_vertex(i[1])
        # build edges
        g.add_edge(i[1], i[0])
    # init a Q and add starting vertex as a list
    q = Queue()
    q.enqueue([starting_node])
    # set max path and earliest ancestor -1 for return if no neighbors
    max_path = 1
    earliest = -1
    # while the Q has elements
    while q.size() > 0:
        # we pull the first element into our path
        path = q.dequeue()
        # set v to the last index of path
        v = path[-1]
        if(len(path) >= max_path and v < earliest) or (len(path) > max_path):
            earliest = v
            max_path = len(path)
        for next_item in g.verts[v]:
            copy = list(path)
            copy.append(next_item)
            q.enqueue(copy)
    return earliest




