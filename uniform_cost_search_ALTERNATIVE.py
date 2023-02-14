# P2-3(19): Graph4 UCS by using VERTICE LIST.  (Osman Bulut-001530539)

from queue import PriorityQueue

verticelist = {
    'a': {},
    'b': {'a': 2},
    'c': {'a': 2},
    'd': {'b': 1, 'c': 8, 'e': 2},
    'e': {'h': 8, 'r': 2},
    'f': {'c': 3, 'g': 2},
    'g': {},
    'h': {'p': 4, 'q': 4},
    'p': {'q': 15},
    'q': {},
    'r': {'f': 2},
    's': {'d': 3, 'e': 9, 'p': 1}
}


def ucs(graph, source, destination):
    expanded = []
    q = PriorityQueue()
    q.put((0, source))
    visited = set()

    while q:

        weight, vertex = q.get()  # we save our current weight of the edge(cost) and vertex
        current = vertex[-1]  # we need to check the last member of our corresponding branch.That's why we used vertex[-1].

        if current not in visited:  # the first sub-loop checks whether our current vertex is visited before. If it is, it will check out the second cheapest vertex.
            visited.add(current)
            expanded.append(
                current)  # if not, we will add it into both our set and list. Bcs we need them distinctively.

            if current == destination:  # second sub-loop checks whether we reach our destination vertex. If it is we will break the main loop by returning 2 variables.
                return vertex, expanded

            children = graph[current]  # if not, we will determine children of our vertex.
            for i in children:
                if i not in visited:  # we'll check out each child to see whether they were visited before. if not, we'll save their totalweight
                    totalweight = weight + children[i]
                    q.put((totalweight,
                           vertex + i))  # total weight of the corresponding branch. These branches are shown in documentation file.


solution, expanded = ucs(verticelist, 's', 'g')
print('The return path is ----> ', solution)
print("The expanded vertex list until reaching the destination is ---->", expanded)
