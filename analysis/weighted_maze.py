##########################################
# For testing cost-aware Dijkstra and A* #
##########################################


import tkinter as tk
from algorithms.recursive_backtracker import RecursiveBacktracker
from algorithms.link_all import LinkAll
from algorithms.sidewinder import Sidewinder
from gui.maze_window import MazeWindow
from maze.custom_grid import CustomGrid
from maze.maze_renderer import MazeRenderer
from maze.text_renderer import TextRenderer

grid = CustomGrid(20, 20)
algorithm = LinkAll()
algorithm.on(grid)

# grid.braid(0.5)  # Optional.

start = grid[11, 0]
finish = grid[1, 13]

# WALLS
row = 2
for column in range(5, 13):
    cell = grid[row, column]
    for neighbor in cell.neighbors():
        if neighbor in cell.links:
            cell.unlink(neighbor)

row = 12
for column in range(2, 13):
    cell = grid[row, column]
    for neighbor in cell.neighbors():
        if neighbor in cell.links:
            cell.unlink(neighbor)

column = 12
for row in range(3, 12):
    cell = grid[row, column]
    for neighbor in cell.neighbors():
        if neighbor in cell.links:
            cell.unlink(neighbor)


root = tk.Tk()

# Dijkstra:
distances = start.distances(finish)
grid.set_distances(distances)
# grid.set_distances(distances.path_to(finish))
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="distances")
# ASCII:
renderer = TextRenderer()
print("distances")
print(renderer.render(grid))

# Dijkstra - priority queue:
distances = start.distances2(finish)
grid.set_distances(distances)
# # grid.set_distances(distances.path_to(finish))
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="distances2")
# ASCII:
renderer = TextRenderer()
print("distances2")
print(renderer.render(grid))

# A-star:
distances = start.astar(finish)
grid.set_distances(distances)
# grid.set_distances(distances.path_to(finish))
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="astar")
# ASCII:
renderer = TextRenderer()
print("astar")
print(renderer.render(grid))

if distances[finish] is None:
    print("No path exists from start to finish.")

root.mainloop()
