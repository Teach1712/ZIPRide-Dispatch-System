# =========================================================
# graph.py
# ZipRide Dispatch System
# =========================================================

from collections import deque


class Graph:

    def __init__(self):
        self.vertices = {}

    # =====================================================
    # Add Location
    # =====================================================

    def add_location(self, location):

        if location not in self.vertices:
            self.vertices[location] = []

    # =====================================================
    # Add Road
    # =====================================================

    def add_road(self, src, dest, weight):

        if weight < 0:
            print("Negative weights are not allowed")
            return

        self.add_location(src)
        self.add_location(dest)

        self.vertices[src].append((dest, weight))
        self.vertices[dest].append((src, weight))

    # =====================================================
    # Print Graph
    # =====================================================

    def print_graph(self):

        print("\nAdjacency List:\n")

        for location in self.vertices:

            print(location + ":")

            if len(self.vertices[location]) == 0:
                print("No roads")

            else:

                for neighbour, weight in self.vertices[location]:
                    print(neighbour + "(" + str(weight) + ")")

            print()

    # =====================================================
    # BFS
    # =====================================================

    def bfs(self, start):

        if start not in self.vertices:
            print("Invalid location")
            return

        visited = []
        queue = deque()

        queue.append((start, 0))
        visited.append(start)

        current_level = -1

        print("\nBFS from", start)

        while queue:

            node, level = queue.popleft()

            if level != current_level:
                current_level = level
                print("\nLevel", level, ":", end=" ")

            print(node, end=" ")

            for neighbour, weight in self.vertices[node]:

                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append((neighbour, level + 1))

        print()

    # =====================================================
    # DFS Cycle Detection
    # =====================================================

    def dfs_cycle(self):

        visited = []

        for node in self.vertices:

            if node not in visited:

                result = self._dfs_recursive(
                    node,
                    visited,
                    None,
                    []
                )

                if result:
                    print("\nCycle detected:")
                    print(" -> ".join(result))
                    return

        print("\nNo cycle detected")

    def _dfs_recursive(self, current, visited, parent, path):

        visited.append(current)
        path.append(current)

        for neighbour, weight in self.vertices[current]:

            if neighbour not in visited:

                result = self._dfs_recursive(
                    neighbour,
                    visited,
                    current,
                    path
                )

                if result:
                    return result

            elif neighbour != parent:

                cycle_path = path.copy()
                cycle_path.append(neighbour)

                return cycle_path

        path.pop()

        return None

    # =====================================================
    # Dijkstra Algorithm
    # =====================================================

    def dijkstra(self, start, end):

        if start not in self.vertices:
            print("Invalid source")
            return

        if end not in self.vertices:
            print("Invalid destination")
            return

        distances = {}
        previous = {}
        visited = []

        for node in self.vertices:
            distances[node] = 999999
            previous[node] = None

        distances[start] = 0

        while len(visited) < len(self.vertices):

            current = None
            smallest = 999999

            for node in self.vertices:

                if node not in visited and distances[node] < smallest:
                    smallest = distances[node]
                    current = node

            if current is None:
                break

            visited.append(current)

            for neighbour, weight in self.vertices[current]:

                new_distance = distances[current] + weight

                if new_distance < distances[neighbour]:
                    distances[neighbour] = new_distance
                    previous[neighbour] = current

        if distances[end] == 999999:
            print("No path exists")
            return

        path = []

        current = end

        while current is not None:
            path.insert(0, current)
            current = previous[current]

        print("\nDijkstra Shortest Path")
        print("Source:", start)
        print("Destination:", end)
        print("Shortest Time:", distances[end], "minutes")
        print("Path:", " -> ".join(path))

        return distances[end]