##########################################
# For testing cost-aware Dijkstra and A* #
##########################################


import random
from maze.grid import Grid
from maze.cell import Cell
from maze_generation.binary_tree import BinaryTree
from maze_generation.sidewinder import Sidewinder
from maze_generation.aldous_broder import AldousBroder
from maze_generation.wilsons import Wilsons
from maze_generation.hunt_and_kill import HuntAndKill
from maze_generation.recursive_backtracker import RecursiveBacktracker
from pathfinding.dijkstra import dijkstra
from pathfinding.astar import astar


algorithms = {
    "BinaryTree": BinaryTree,
    "Sidewinder": Sidewinder,
    "AldousBroder": AldousBroder,
    "Wilsons": Wilsons,
    "HuntAndKill": HuntAndKill,
    "RecursiveBacktracker": RecursiveBacktracker
}


def validate_search(grid) -> tuple[Cell, Cell, int, int]:
    """Checks that both algorithms find the path with the same cost."""

    start = grid.random_cell()
    goal = grid.random_cell()

    while start == goal:
        goal = grid.random_cell()

    dijkstra_distances = dijkstra(start, goal)
    astar_distances = astar(start, goal)

    dijkstra_cost = dijkstra_distances[goal]
    astar_cost = astar_distances[goal]

    if dijkstra_cost is None:
        raise AssertionError("Dijkstra did not find a path.")
    if astar_cost is None:
        raise AssertionError("A* did not find a path.")
    if dijkstra_cost != astar_cost:
        raise AssertionError(
            f"Different cost paths: "
            f"Dijkstra: {dijkstra_cost}, A*: {astar_cost}"
        )

    return start, goal, dijkstra_cost, astar_cost


def main():
    # (1.) Path comparison:
    random.seed(2026)

    rows = 20
    columns = 20
    repetitions = 20
    successful_tests = 0

    print()
    print(f"Repetitions: {repetitions} | Rows: {rows} | Columns: {columns}\n")

    for algorithm_name, algorithm_class in algorithms.items():
        for repetition in range(repetitions):
            grid = Grid(rows, columns)

            maze_algorithm = algorithm_class()
            maze_algorithm.on(grid)

            validate_search(grid)

            successful_tests += 1

        print("{:>20} tests passed: {:>3}".format(algorithm_name, repetitions))

    print()
    print((" " * 15) + "Total tests passed: {}".format(successful_tests))

    # (2.) Cell count comparison:
    random.seed(2026)

    repetitions = 100
    rows, columns = 20, 20

    print()
    print(f"Repetitions: {repetitions} | Rows: {rows} | Columns: {columns}\n")

    total_cumulative_dijkstra_cells = 0
    total_cumulative_astar_cells = 0
    total_cumulative_path_length = 0

    for algorithm_name, algorithm_class in algorithms.items():
        cumulative_dijkstra_distances = 0
        cumulative_astar_distances = 0
        cumulative_path_length = 0

        for repetition in range(repetitions):
            grid = Grid(rows, columns)

            maze_algorithm = algorithm_class()
            maze_algorithm.on(grid)

            start = grid.random_cell()
            goal = grid.random_cell()
            while start == goal:
                goal = grid.random_cell()

            dijkstra_distances = dijkstra(start, goal)
            astar_distances = astar(start, goal)

            # Number of cells in a path:
            astar_path_cell_number = len(astar_distances.path_to(goal).cells())
            cumulative_path_length += astar_path_cell_number
            total_cumulative_path_length += astar_path_cell_number

            dijkstra_cells = dijkstra_distances.cells()
            astar_cells = astar_distances.cells()

            cumulative_dijkstra_distances += len(dijkstra_cells)
            cumulative_astar_distances += len(astar_cells)

            total_cumulative_dijkstra_cells += len(dijkstra_cells)
            total_cumulative_astar_cells += len(astar_cells)

        avg_dijkstra_cells = cumulative_dijkstra_distances / repetitions
        avg_astar_cells = cumulative_astar_distances / repetitions

        print("{:>20} average dijkstra cells: {:.2f}".format(algorithm_name, avg_dijkstra_cells))
        print("{:>23} average astar cells: {:.2f}".format(algorithm_name, avg_astar_cells))
        # Calculate % difference:
        cell_difference = abs(avg_dijkstra_cells - avg_astar_cells)
        if avg_dijkstra_cells < avg_astar_cells:
            raise AssertionError("Dijkstra is better than A*.")
        elif avg_dijkstra_cells == avg_astar_cells:
            print("Dijkstra and A* have the same number of cells.")
        else:
            percent_diff = cell_difference / avg_dijkstra_cells * 100
            print((" " * 10) + "A* is {:.2f}% better than Dijkstra.".format(percent_diff))

        avg_path_length = cumulative_path_length / repetitions
        print((" " * 24) +  "Average path length: {:.2f}".format(avg_path_length))
        print()

    total_avg_cumulative_dijkstra_cells = total_cumulative_dijkstra_cells / (len(algorithms) * repetitions)
    total_avg_cumulative_astar_cells = total_cumulative_astar_cells / (len(algorithms) * repetitions)

    print(" " * 15 + "Total average dijkstra cells: {:.2f}".format(total_avg_cumulative_dijkstra_cells))
    print(" " * 18 + "Total average astar cells: {:.2f}".format(total_avg_cumulative_astar_cells))

    cell_global_difference = abs(total_avg_cumulative_dijkstra_cells - total_avg_cumulative_astar_cells)
    if total_avg_cumulative_dijkstra_cells < total_avg_cumulative_astar_cells:
        raise AssertionError("Dijkstra is better than A*.")
    elif total_avg_cumulative_dijkstra_cells == total_avg_cumulative_astar_cells:
        print("Dijkstra and A* have the same number of cells.")
    else:
        percent_diff = cell_global_difference / total_avg_cumulative_dijkstra_cells * 100
        print((" " * 10) + "A* is {:.2f}% better than Dijkstra.".format(percent_diff))

    total_avg_cumulative_path_length = total_cumulative_path_length / (len(algorithms) * repetitions)
    print((" " * 18) +  "total average path length: {:.2f}".format(total_avg_cumulative_path_length))


if __name__ == "__main__":
    main()
