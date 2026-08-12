import tkinter as tk
from maze.grid import Grid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from algorithms.link_all import LinkAll
from maze.text_renderer import TextRenderer

grid = Grid(20, 20)
algorithm = LinkAll()
algorithm.on(grid)

renderer = TextRenderer()
print(renderer.render(grid))

root = tk.Tk()
renderer = MazeRenderer()
image = renderer.render(grid)
window = MazeWindow(root, image, title="Link All Demo")
root.mainloop()
