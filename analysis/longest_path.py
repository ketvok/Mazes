################################################
# For finding the longest path through a maze. #
# Can be used to make challenging mazes.       #
################################################


from maze.grid import Grid
from maze.text_renderer import TextRenderer
from maze_generation.binary_tree import BinaryTree
from pathfinding.dijkstra import dijkstra


grid = Grid(8, 8)
algorithm = BinaryTree()
algorithm.on(grid)

# 1. Choose a starting cell.
start = grid[0, 0]

# 2. Find the cell with the maximum distance from the starting cell.
distances = dijkstra(start)  # Store distances from start to every other reachable cell.
new_start, distance = distances.max()  # Return the cell with the maximum distance.

# 3. Repeat step 2 with the cell that had maximum distance from the starting cell as the new starting cell.
new_distances = dijkstra(new_start)  # Store distances from new_start to every other reachable cell.
goal, distance = new_distances.max()  # Return the cell with the maximum distance.

# 4. Print the path from the starting cell to the goal cell.
grid.distances = new_distances.path_to(goal)
renderer = TextRenderer()
print(renderer.render(grid))

# Note:
# This is technically the longest path. There may be multiple paths through the maze that are all equally long,
# and thus equally longest.
