########################################################
# Print the average dead-end count for each algorithm. #
########################################################


from maze.grid import Grid
from algorithms.binary_tree import BinaryTree
from algorithms.sidewinder import Sidewinder
from algorithms.aldous_broder import AldousBroder
from algorithms.wilsons import Wilsons
from algorithms.hunt_and_kill import HuntAndKill
from algorithms.recursive_backtracker import RecursiveBacktracker


ALGORITHMS = [BinaryTree, Sidewinder, AldousBroder, Wilsons, HuntAndKill, RecursiveBacktracker]

tries = 10  # Number of times to run each algorithm.
size = 20  # Size of the maze.

averages = {}  # Dictionary to store average dead-end counts for each algorithm.

for algorithm in ALGORITHMS:
    print("Running {}...".format(algorithm.__name__))
    deadend_counts = []  # List to store dead-end counts for each run.
    for _ in range(tries):
        grid = Grid(size, size)
        algorithm().on(grid)
        deadend_counts.append(len(grid.deadends()))
    total_dead_ends = sum(deadend_counts)
    averages[algorithm] = total_dead_ends / len(deadend_counts)

total_cells = size * size
print("Average dead-ends per {}x{} maze ({} cells):".format(size, size, total_cells))

# "sorted" returns an ordered list of pairs (Algorithm, average dead ends).
sorted_averages = sorted(averages.items(), key=lambda x: -x[1])

for algorithm, average in sorted_averages:  # Python unpacks the pair into two variables.
    percentage = average * 100.0 / total_cells
    print(" {:>20}: {:>3.0f}/{:>3d} ({:.0f}%)".format(algorithm.__name__, average, total_cells, percentage))
