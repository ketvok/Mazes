from queue import PriorityQueue
from itertools import count
from maze.cell import Cell
from maze.distances import Distances
from pathfinding.heuristics import manhattan_distance


def astar(start, goal) -> Distances:
    """
    Compute the weighted shortest path to goal using A* algorithm.

    Version using priority queue.
    """

    weights = Distances(start)  # Shortest distances to the start node. Starts with start as start (distance 0).

    frontier = PriorityQueue[tuple[int, int, Cell]]()
    counter = count()
    frontier.put((0, next(counter), start))

    while not frontier.empty():
        # (1.) Find the unprocessed node with minimal distance to the start node:
        _, _, cell = frontier.get()

        if cell == goal:
            break

        # (2.) Relax distances to nodes that are reachable from current node:
        for neighbor in cell.links:
            new_weight = weights[cell] + neighbor.weight

            if weights[neighbor] is None or \
            new_weight < weights[neighbor]:
                weights[neighbor] = new_weight
                heuristic = manhattan_distance(goal, neighbor)

                priority = new_weight + heuristic
                frontier.put((priority, next(counter), neighbor))

    return weights