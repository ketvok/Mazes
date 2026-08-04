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

        weights = Distances(self)  # Shortest distances to the start node. Starts with self as start (distance 0).
        pending = [self]  # Start with self as the only cell in the pending list.

        while pending:
            # (1.) Find unprocessed node with minimal distance to starting node and remove it from pending.
            cell = min(pending, key=lambda c: weights[c])  # Get the cell from the pending list with the lowest weight.

            if cell == goal:
                break

            pending.remove(cell)  # Remove the cell from the pending list (it's been visited).

            # (2.) Relax distances to nodes that are reachable from current node.
            for neighbor in cell.links:  # Iterate over nodes we can reach from current node.
                total_weight = weights[cell] + neighbor.weight  # Weight of reaching the neighbor from current node.

                # If the weight of reaching the neighbor from current node is less than the total weight of the shortest
                # path...
                if weights[neighbor] is None or total_weight < weights[neighbor]:
                    pending.append(neighbor)
                    weights[neighbor] = total_weight  # ...relax distance to neighbor.

        return weights

    # Note: this is not a textbook version of Dijkstra. It has no "done" or "visited" set, but only "frontier" or
    # "pending" cells. A cell can be in the pending set more than once (if it's reachable from multiple nodes).
    # For example, cells A, B and C. We start from cell A, relax distances to cells B and C. Add B and C to pending.
    # We go to cell from pending with the shortest distance, which is C. Relax distances to cells B again, because
    # it's better than going through A. Add B to pending again. Now pending contains [B, B].

    def distances2(self, goal = None) -> Distances:
        """
        Compute weighted shortest paths using Dijkstra's algorithm.

        Version using priority queue.
        """

        weights = Distances(self)  # Shortest distances to the start node. Starts with self as start (distance 0).

        frontier = PriorityQueue()
        counter = count()
        frontier.put((0, next(counter), self))

        while not frontier.empty():
            _, _, cell = frontier.get()

            if cell == goal:
                break

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

        frontier = PriorityQueue()
        counter = count()
        frontier.put((0, next(counter), self))

        while not frontier.empty():
            _, _, cell = frontier.get()

            if cell == goal:
                break

            for neighbor in cell.links:
                new_weight = weights[cell] + neighbor.weight

                if weights[neighbor] is None or new_weight < weights[neighbor]:
                    weights[neighbor] = new_weight
                    heuristic = manhattan_distance(goal, neighbor)
                    priority = new_weight + heuristic
                    frontier.put((priority, next(counter), neighbor))

        return weights
