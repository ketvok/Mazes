##########################################
# For testing cost-aware Dijkstra and A* #
##########################################


import tkinter as tk
from algorithms.recursive_backtracker import RecursiveBacktracker
from algorithms.link_all import LinkAll
from algorithms.sidewinder import Sidewinder
from maze.custom_grid import CustomGrid


grid = CustomGrid(20, 20)
algorithm = Sidewinder()
# algorithm = LinkAll()
algorithm.on(grid)

# grid.braid(0.1)

# start = grid[0, 0]
# finish = grid[grid.rows - 1, grid.columns - 1]




# distances = start.distances()
# grid.set_distances(distances)
# grid.set_distances(distances.path_to(finish))

# grid.to_png()




# lava = choice(grid.distances.cells())
# lava.weight = 50
#
# distances = start.distances()
# grid.set_distances(distances.path_to(finish))
#
# grid.to_png()




# A*

start = grid[0, 0]
finish = grid[19, 19]

# WALLS
# row = 2
# for column in range(5, 13):
#     cell = grid[row, column]
#     for neighbor in cell.neighbors():
#         if neighbor in cell.links:
#             cell.unlink(neighbor)
#
# row = 12
# for column in range(2, 13):
#     cell = grid[row, column]
#     for neighbor in cell.neighbors():
#         if neighbor in cell.links:
#             cell.unlink(neighbor)
#
# column = 12
# for row in range(3, 12):
#     cell = grid[row, column]
#     for neighbor in cell.neighbors():
#         if neighbor in cell.links:
#             cell.unlink(neighbor)


# distances = start.distances(finish)
# grid.set_distances(distances)
# # grid.set_distances(distances.path_to(finish))
# grid.to_png()
#
# # Pause 2 seconds:
# time.sleep(2)
#
# distances = start.distances2(finish)
# grid.set_distances(distances)
# # grid.set_distances(distances.path_to(finish))
# grid.to_png()
#
# # Pause 2 seconds:
# time.sleep(2)

distances = start.astar(finish)
# grid.set_distances(distances)
grid.set_distances(distances.path_to(finish))

grid.to_s()

root = tk.Tk()

grid.to_png()
root.mainloop()
