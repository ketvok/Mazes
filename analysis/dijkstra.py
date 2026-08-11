#######################
# Visalize Dijkstra's #
#######################


import tkinter as tk
from maze.distance_grid import DistanceGrid
from algorithms.sidewinder import Sidewinder
from maze.colored_grid import ColoredGrid
from algorithms.recursive_backtracker import RecursiveBacktracker


#########################
# Create a maze (ASCII)
#-----------------------------------------------------------------------------------------------------------------------
# Make a distance grid.
grid = DistanceGrid(10, 10)

# Make a maze out of grid using a specific algorithm.
algorithm = Sidewinder()
algorithm.on(grid)

# Assign a start cell, calculate distances and store them to grid.
start = grid[0, 0]
distances = start.distances()  # Variable distances has distances from start to every other cell.
grid.distances = distances
#-----------------------------------------------------------------------------------------------------------------------

# Optional: draw only distance to goal.
#-----------------------------------------------------------------------------------------------------------------------
grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
#-----------------------------------------------------------------------------------------------------------------------

# Draw a maze with distance to the goal.
#-----------------------------------------------------------------------------------------------------------------------
grid.to_s()
#-----------------------------------------------------------------------------------------------------------------------


########################################################################################################################


#######################
# Create a maze (PNG)
#-----------------------------------------------------------------------------------------------------------------------
# Make a colored grid.
grid = ColoredGrid(20, 20)

# Make a maze out of the grid using a specific algorithm.
algorithm = RecursiveBacktracker()
algorithm.on(grid)

# Optional: Define braiding factor.
grid.braid(0.1)

# Assign a start cell, calculate distances and store them to grid.
start = grid[0, 0]
distances = start.distances()  # Distances stores starting cell and path to all other reachable cells.
grid.distances = distances  # Store that info to grid.

# Optional: color only path to goal.
#-----------------------------------------------------------------------------------------------------------------------
grid.distances = distances.path_to(grid[grid.rows - 1, grid.columns - 1])
#-----------------------------------------------------------------------------------------------------------------------

# Draw a maze.
#-----------------------------------------------------------------------------------------------------------------------
root = tk.Tk()

grid.to_png(parent=root, title="Dijkstra")
root.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
