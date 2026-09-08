########################################################
# Print the average dead-end count for each algorithm. #
########################################################


from maze.grid import Grid
from maze_generation.binary_tree import BinaryTree
from maze_generation.sidewinder import Sidewinder
from maze_generation.aldous_broder import AldousBroder
from maze_generation.wilsons import Wilsons
from maze_generation.hunt_and_kill import HuntAndKill
from maze_generation.recursive_backtracker import RecursiveBacktracker


ALGORITHMS = [BinaryTree, Sidewinder, AldousBroder, Wilsons, HuntAndKill, RecursiveBacktracker]

tries = 10  # Number of times to run each algorithm.
size = 20  # Size of the maze.

averages = {}  # Dictionary to store average dead-end counts for each algorithm.

for algorithm in ALGORITHMS:
    print("Running {}...".format(algorithm.__name__))
    dead_end_counts = []  # List to store dead-end counts for each run.
    for _ in range(tries):
        grid = Grid(size, size)
        algorithm().on(grid)
        dead_end_counts.append(len(grid.dead_ends()))
    total_dead_ends = sum(dead_end_counts)
    averages[algorithm] = total_dead_ends / len(dead_end_counts)

total_cells = size * size
print("Average dead-ends per {}x{} maze ({} cells):".format(size, size, total_cells))

# "sorted" returns an ordered list of pairs (Algorithm, average dead ends).
sorted_averages = sorted(averages.items(), key=lambda x: -x[1])

for algorithm, average in sorted_averages:  # Python unpacks the pair into two variables.
    percentage = average * 100.0 / total_cells
    print(" {:>20}: {:>3.0f}/{:>3d} ({:.0f}%)".format(algorithm.__name__, average, total_cells, percentage))
