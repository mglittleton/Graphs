"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        printed_traversal = ""
        viewed = {}
        for vert in self.vertices:
            viewed[vert] = "white"

        viewed[starting_vertex] = "gray"
        queue = Queue()
        queue.enqueue(starting_vertex)

        while len(queue.queue) > 0:
            head = queue.queue[0]
            for vert in self.vertices[head]:
                if viewed[vert] == "white":
                    viewed[vert] = "gray"
                    queue.enqueue(vert)
            comma = ", " if printed_traversal != "" else ""
            printed_traversal += comma + str(queue.dequeue())
            viewed[head] = 'black'
        print(printed_traversal)

    def dft(self, starting_vertex):
        printed_traversal = ''
        viewed = {}
        for vert in self.vertices:
            viewed[vert] = False

        stack = Stack()
        stack.push(starting_vertex)
        viewed[starting_vertex] = True

        while len(stack.stack) > 0:
            tail = stack.pop()
            comma = ", " if printed_traversal != "" else ""
            printed_traversal += comma + str(tail)

            for vert in self.vertices[tail]:
                if not viewed[vert]:
                    viewed[vert] = True
                    stack.push(vert)

        print(printed_traversal)

    def dft_recursive(self, starting_vertex):
        # printed_traversal = ''

        # viewed = {}
        # for vert in self.vertices:
        #     viewed[vert] = True if vert == starting_vertex else False

        # def recursion(self, vertex):
        #     for vert in self.vertices[vertex]:
        #         if not viewed[vert]:
        #             viewed[vert] = True
        #             self.recursion(vert)
        pass

    def bfs(self, starting_vertex, destination_vertex):
        visited_paths = {}
        queue = Queue()
        queue.enqueue([starting_vertex])
        while not destination_vertex in visited_paths:
            curr_path = queue.dequeue()
            curr_node = curr_path[-1]
            if curr_node not in visited_paths:
                visited_paths[curr_node] = curr_path
                for vert in self.vertices[curr_node]:
                    if vert not in visited_paths:
                        new_path = list(curr_path)
                        new_path.append(vert)
                        queue.enqueue(new_path)
            if len(self.vertices) == len(visited_paths) and destination_vertex not in visited_paths:
              visited_paths[destination_vertex] = None
        return visited_paths[destination_vertex]

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO


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
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

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
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
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
