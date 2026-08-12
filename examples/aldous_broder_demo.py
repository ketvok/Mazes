import tkinter as tk
from maze.grid import Grid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from algorithms.aldous_broder import AldousBroder
from maze.text_renderer import TextRenderer

grid = Grid(20, 20)
algorithm = AldousBroder()
algorithm.on(grid)

grid.braid(0.2)  # Optional.

renderer = TextRenderer()
print(renderer.render(grid))

root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Aldous Broder Demo")
root.mainloop()
