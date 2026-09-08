##########################################
# For testing cost-aware Dijkstra and A* #
##########################################


import tkinter as tk
from maze.grid import Grid
from maze_generation.recursive_backtracker import RecursiveBacktracker
from maze_generation.link_all import LinkAll
from maze_generation.sidewinder import Sidewinder
from gui.maze_window import MazeWindow
from maze.maze_renderer import MazeRenderer
from maze.text_renderer import TextRenderer
from pathfinding.dijkstra import dijkstra
from pathfinding.astar import astar

grid = Grid(20, 20)
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

# # Dijkstra:
# distances = dijkstra(start, finish)
# grid.set_distances(distances)
# # grid.set_distances(distances.path_to(finish))
# renderer = MazeRenderer()
# image = renderer.render(grid)
# window = MazeWindow(root, image, title="distances")
# # ASCII:
# renderer = TextRenderer()
# print("distances")
# print(renderer.render(grid))

# Dijkstra - priority queue:
distances = dijkstra(start, finish)
grid.set_distances(distances)
# # grid.set_distances(distances.path_to(finish))
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="dijkstra")
# ASCII:
renderer = TextRenderer()
print("dijkstra")
print(renderer.render(grid))

# A-star:
distances = astar(start, finish)
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
