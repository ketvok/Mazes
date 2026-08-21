from queue import PriorityQueue
from itertools import count
from maze.cell import Cell
from maze.distances import Distances


def manhattan_distance(cell1, cell2):
    return abs(cell1.row - cell2.row) + abs(cell1.column - cell2.column)


class WeightedCell(Cell):
    """Defines a weighted cell in a grid."""

    def __init__(self, row, column) -> None:
        super().__init__(row, column)
        self.weight = 1  # Default movement cost to this cell.

    def distances(self, goal = None) -> Distances:
        """
        Compute weighted shortest paths using Dijkstra's algorithm.

        Version using a list of pending cells.
        """

        weights = Distances(self)  # Lowest distances (weights) to the start node. Starts with self as start (distance 0).
        pending = [self]  # Start with self as the only cell in the pending list.

        while pending:
            # (1.) Find the unprocessed node with minimal distance to the start node:
            cell = min(pending, key=lambda c: weights[c])  # Get the cell from the pending list with the lowest distance.

            if cell == goal:
                break

            pending.remove(cell)  # (it's been visited / reached).

            # (2.) Relax distances to nodes that are reachable from current node:
            for neighbor in cell.links:  # Nodes we can reach from current node.
                new_weight = weights[cell] + neighbor.weight  # Distance of reaching a neighboring node from the current node.

                # If neighbor was not previously visited, or if the weight of reaching the neighbor from the current node
                # is less than the previously recorded weight...
                if weights[neighbor] is None or new_weight < weights[neighbor]:
                    pending.append(neighbor)
                    weights[neighbor] = new_weight  # ...relax distance to neighbor.

        return weights

    def distances2(self, goal = None) -> Distances:
        """
        Compute weighted shortest paths using Dijkstra's algorithm.

        Version using priority queue.
        """

        weights = Distances(self)  # Shortest distances to the start node. Starts with self as start (distance 0).

        frontier =  PriorityQueue[tuple[int, int, WeightedCell]]()
        counter = count()
        frontier.put((0, next(counter), self))

        while not frontier.empty():
            # (1.) Find the unprocessed node with minimal distance to the start node:
            _, _, cell = frontier.get()

            if cell == goal:
                break

            # (2.) Relax distances to nodes that are reachable from current node:
            for neighbor in cell.links:
                new_weight = weights[cell] + neighbor.weight

                if weights[neighbor] is None or new_weight < weights[neighbor]:
                    weights[neighbor] = new_weight

                    priority = new_weight
                    frontier.put((priority, next(counter), neighbor))

        return weights

    def astar(self, goal) -> Distances:
        """
        Compute the weighted shortest path to goal using A* algorithm.

        Version using priority queue.
        """

        weights = Distances(self)  # Shortest distances to the start node. Starts with self as start (distance 0).

        frontier = PriorityQueue[tuple[int, int, WeightedCell]]()
        counter = count()
        frontier.put((0, next(counter), self))

        while not frontier.empty():
            # (1.) Find the unprocessed node with minimal distance to the start node:
            _, _, cell = frontier.get()

            if cell == goal:
                break

            # (2.) Relax distances to nodes that are reachable from current node:
            for neighbor in cell.links:
                new_weight = weights[cell] + neighbor.weight

                if weights[neighbor] is None or new_weight < weights[neighbor]:
                    weights[neighbor] = new_weight
                    heuristic = manhattan_distance(goal, neighbor)

                    priority = new_weight + heuristic
                    frontier.put((priority, next(counter), neighbor))

        return weights
