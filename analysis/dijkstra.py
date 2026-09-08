#######################
# Visalize Dijkstra's #
#######################


import tkinter as tk
from maze.grid import Grid
from maze.text_renderer import TextRenderer
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from maze_generation.sidewinder import Sidewinder
from maze_generation.recursive_backtracker import RecursiveBacktracker
from pathfinding.dijkstra import dijkstra


#########################
# Create a maze (ASCII)
#-----------------------------------------------------------------------------------------------------------------------
# Make a distance grid.
grid = Grid(10, 10)

# Make a maze out of grid using a specific algorithm.
algorithm = Sidewinder()
algorithm.on(grid)

# Assign a start cell, calculate distances and store them to grid.
start = grid[0, 0]
distances = dijkstra(start)  # Store distances from start to every other reachable cell.
grid.distances = distances
#-----------------------------------------------------------------------------------------------------------------------

# Optional: draw only distance to goal.
#-----------------------------------------------------------------------------------------------------------------------
grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
#-----------------------------------------------------------------------------------------------------------------------

# Draw a maze with distance to the goal.
#-----------------------------------------------------------------------------------------------------------------------
renderer = TextRenderer()
print(renderer.render(grid))
#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################


#######################
# Create a maze (PNG)
#-----------------------------------------------------------------------------------------------------------------------
# Make a colored grid.
grid = Grid(20, 20)

# Make a maze out of the grid using a specific algorithm.
algorithm = RecursiveBacktracker()
algorithm.on(grid)

# Optional: Define braiding factor.
grid.braid(0.1)

# Assign a start cell, calculate distances and store them to grid.
start = grid[0, 0]
distances = dijkstra(start)  # Store distances from start to every other reachable cell.
grid.distances = distances  # Store that info to grid.

# Optional: color only path to goal.
#-----------------------------------------------------------------------------------------------------------------------
grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
#-----------------------------------------------------------------------------------------------------------------------

# Draw a maze.
#-----------------------------------------------------------------------------------------------------------------------
root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Dijkstra")
root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
