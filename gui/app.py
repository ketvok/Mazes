import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as tk_font
from maze.grid import Grid
from maze.maze_renderer import MazeRenderer
from gui.maze_window import MazeWindow
from maze_generation.binary_tree import BinaryTree
from maze_generation.sidewinder import Sidewinder
from maze_generation.aldous_broder import AldousBroder
from maze_generation.wilsons import Wilsons
from maze_generation.hunt_and_kill import HuntAndKill
from maze_generation.recursive_backtracker import RecursiveBacktracker
from pathfinding.dijkstra import dijkstra
from pathfinding.astar import astar


class App(tk.Tk):
    """
    This class represents the main application window for a maze generator and
    pathfinder tool.
    """

    def __init__(self):
        super().__init__()
        self.renderer = MazeRenderer()
        self.grid = None
        self.distances = None
        self.start = None
        self.goal = None
        self.defaults = {
            "rows": "20",
            "columns": "20"
        }
        self.search_algorithm_name = None

        # Window settings
        self.title("Mazes")
        self.resizable(False, False)

        # Validation settings
        v_rows_columns = (self.register(self.validate_rows_columns), '%P')
        v_start_x = (self.register(self.validate_start_x), '%P')
        v_start_y = (self.register(self.validate_start_y), '%P')
        v_goal_x = (self.register(self.validate_goal_x), '%P')
        v_goal_y = (self.register(self.validate_goal_y), '%P')

        # Font setup
        font_size = 14
        my_font = tk_font.Font(family="Helvetica", size=font_size)
        self.option_add("*TCombobox*Listbox*Font", my_font)  # Apply the font to all combo boxes and list boxes.

        # Maze Algorithm
        self.lbl_maze = tk.Label(self, text="Maze Algorithm:", font=my_font, pady=10)
        self.lbl_maze.grid(column=0, row=0, sticky="w")

        self.var_maze = tk.StringVar(self)
        self.maze_items = [
            "Binary Tree",
            "Sidewinder",
            "Aldous Broder",
            "Wilson's",
            "Hunt and Kill",
            "Recursive Backtracker"
        ]
        self.maze = ttk.Combobox(self, state="readonly", textvariable=self.var_maze, values=self.maze_items, font=my_font)
        self.var_maze.set(self.maze_items[0])  # Default value.
        self.maze.bind("<<ComboboxSelected>>", self.maze_config_changed)
        self.maze.grid(column=2, row=0, columnspan=3, sticky="w")

        # Rows
        self.lbl_rows = tk.Label(self, text="Rows:", font=my_font, pady=10)
        self.lbl_rows.grid(column=0, row=1, sticky="w")
        self.ent_rows = tk.Entry(self, font=my_font, validate="key", validatecommand=v_rows_columns, width=5)
        self.ent_rows.insert(0, self.defaults["rows"])
        self.ent_rows.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_rows.bind("<KeyRelease>", self.maze_config_changed)
        self.ent_rows.grid(column=2, row=1, sticky="w")

        # Columns
        self.lbl_columns = tk.Label(self, text="Columns:", font=my_font, pady=10)
        self.lbl_columns.grid(column=0, row=2, sticky="w")
        self.ent_columns = tk.Entry(self, font=my_font, validate="key", validatecommand=v_rows_columns, width=5)
        self.ent_columns.insert(0, self.defaults["columns"])
        self.ent_columns.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_columns.bind("<KeyRelease>", self.maze_config_changed)
        self.ent_columns.grid(column=2, row=2, sticky="w")

        # Start
        self.lbl_start = tk.Label(self, text="Start:", font=my_font, pady=10)
        self.lbl_start.grid(column=0, row=3, sticky="w")

        self.lbl_start_x = tk.Label(self, text="x:", font=my_font, pady=10)
        self.lbl_start_x.grid(column=1, row=3, sticky="e")
        self.ent_start_x = tk.Entry(self, font=my_font, validate="key", validatecommand=v_start_x, width=5)
        self.ent_start_x.insert(0, "0")
        self.ent_start_x.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_start_x.bind("<KeyRelease>", self.start_goal_changed)
        self.ent_start_x.grid(column=2, row=3, sticky="w")

        self.lbl_start_y = tk.Label(self, text="y:", font=my_font, pady=10)
        self.lbl_start_y.grid(column=2, row=3, sticky="e")
        self.ent_start_y = tk.Entry(self, font=my_font, validate="key", validatecommand=v_start_y, width=5)
        self.ent_start_y.insert(0, "0")
        self.ent_start_y.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_start_y.bind("<KeyRelease>", self.start_goal_changed)
        self.ent_start_y.grid(column=3, row=3, sticky="w")

        # Goal
        self.lbl_goal = tk.Label(self, text="Goal:", font=my_font, pady=10)
        self.lbl_goal.grid(column=0, row=4, sticky="w")

        self.lbl_goal_x = tk.Label(self, text="x:", font=my_font, pady=10)
        self.lbl_goal_x.grid(column=1, row=4, sticky="e")
        self.ent_goal_x = tk.Entry(self, font=my_font, validate="key", validatecommand=v_goal_x, width=5)
        self.ent_goal_x.insert(0, str(int(self.ent_rows.get()) - 1))
        self.ent_goal_x.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_goal_x.bind("<KeyRelease>", self.start_goal_changed)
        self.ent_goal_x.grid(column=2, row=4, sticky="w")

        self.lbl_goal_y = tk.Label(self, text="y:", font=my_font, pady=10)
        self.lbl_goal_y.grid(column=2, row=4, sticky="e")
        self.ent_goal_y = tk.Entry(self, font=my_font, validate="key", validatecommand=v_goal_y, width=5)
        self.ent_goal_y.insert(0, str(int(self.ent_columns.get()) - 1))
        self.ent_goal_y.bind("<FocusOut>", self.set_safe_defaults)
        self.ent_goal_y.bind("<KeyRelease>", self.start_goal_changed)
        self.ent_goal_y.grid(column=3, row=4, sticky="w")

        # Search Algorithm
        self.lbl_search = tk.Label(self, text="Search Algorithm:", font=my_font, pady=10)
        self.lbl_search.grid(column=0, row=5, sticky="w")

        self.var_search = tk.StringVar(self)
        self.search_items = [
            "A-star",
            "Dijkstra"
        ]
        self.search = ttk.Combobox(self, state="readonly", textvariable=self.var_search, values=self.search_items, font=my_font)
        self.var_search.set(self.search_items[0])  # Default value.
        self.search.bind("<<ComboboxSelected>>", self.search_algorithm_changed)
        self.search.grid(column=2, row=5, columnspan=3, sticky="w")

        # Frame for Buttons
        self.frm_buttons = tk.Frame(self)
        self.frm_buttons.grid(column=0, columnspan=5, row=6, sticky="w")
        self.frm_buttons.columnconfigure(0, weight=1, uniform="buttons")
        self.frm_buttons.columnconfigure(1, weight=1, uniform="buttons")
        self.frm_buttons.columnconfigure(2, weight=1, uniform="buttons")

        # Maze Buton
        self.btn_maze = tk.Button(self.frm_buttons, text="Maze", command=self.generate_maze, font=my_font)
        self.btn_maze.bind("<Button-1>", self.set_safe_defaults)
        self.btn_maze.grid(column=0, row=0, sticky="nsew")

        # Search Button
        self.btn_search = tk.Button(self.frm_buttons, text="Search", command=self.run_search, font=my_font, state="disabled")
        self.btn_search.grid(column=1, row=0, sticky="nsew")

        # Path Button
        self.btn_path = tk.Button(self.frm_buttons, text="Path", command=self.find_path, font=my_font, state="disabled")
        self.btn_path.grid(column=2, row=0, sticky="nsew")

        # Last Search Label
        self.lbl_last_search = tk.Label(self.frm_buttons, font=my_font, anchor="w", text="", width=20)
        self.lbl_last_search.grid(column=3, row=0)


    ##########################################################################
    #                           Validation Methods                           #
    ##########################################################################

    def validate_rows_columns(self, wanted_value) -> bool:
        """
        Validation for the rows and columns fields.

        Allowed values: 1-100, ASCII digits greater than or equal to 1, no leading zeros.
        """

        # Allow the user to temporarily empty the field with backspace.
        if wanted_value == "":
            return True

        # Only allow ascii digits.
        if not wanted_value.isascii() or not wanted_value.isdigit():
            return False

        # Don't allow leading zeros.
        if wanted_value.startswith("0"):
            return False

        return 1 <= int(wanted_value) <= 100

    def validate_start_x(self, wanted_value) -> bool:
        """Validation for the start x field."""

        # Allow the user to temporarily empty the field with backspace.
        if wanted_value == "":
            return True

        # Only allow ascii digits.
        if not wanted_value.isascii() or not wanted_value.isdigit():
            return False

        # Don't allow leading zeros.
        if len(wanted_value) > 1:
            if wanted_value.startswith("0"):
                return False

        return 0 <= int(wanted_value) <= int(self.ent_rows.get()) - 1

    def validate_start_y(self, wanted_value) -> bool:
        """Validation for the start y field."""

        # Allow the user to temporarily empty the field with backspace.
        if wanted_value == "":
            return True

        # Only allow ascii digits.
        if not wanted_value.isascii() or not wanted_value.isdigit():
            return False

        # Don't allow leading zeros.
        if len(wanted_value) > 1:
            if wanted_value.startswith("0"):
                return False

        return 0 <= int(wanted_value) <= int(self.ent_columns.get())-1

    def validate_goal_x(self, wanted_value) -> bool:
        """Validation for the goal x field."""

        # Allow the user to temporarily empty the field with backspace.
        if wanted_value == "":
            return True

        # Only allow ascii digits.
        if not wanted_value.isascii() or not wanted_value.isdigit():
            return False

        # Don't allow leading zeros.
        if len(wanted_value) > 1:
            if wanted_value.startswith("0"):
                return False

        return 0 <= int(wanted_value) <= int(self.ent_rows.get())-1

    def validate_goal_y(self, wanted_value) -> bool:
        """Validation for the goal y field."""

        # Allow the user to temporarily empty the field with backspace.
        if wanted_value == "":
            return True

        # Only allow ascii digits.
        if not wanted_value.isascii() or not wanted_value.isdigit():
            return False

        # Don't allow leading zeros.
        if len(wanted_value) > 1:
            if wanted_value.startswith("0"):
                return False

        return 0 <= int(wanted_value) <= int(self.ent_columns.get())-1

    def set_safe_defaults(self, event) -> None:
        """Upon focus loss, compare values from different entries and set safe defaults if necessary."""

        if self.ent_start_x.get() == "":
            self.ent_start_x.insert(0, "0")

        if self.ent_start_y.get() == "":
            self.ent_start_y.insert(0, "0")

        if self.ent_goal_x.get() == "":
            self.ent_goal_x.insert(0, "0")

        if self.ent_goal_y.get() == "":
            self.ent_goal_y.insert(0, "0")

        if self.ent_rows.get() == "":
            self.ent_rows.insert(0, "1")
        else:
            rows = int(self.ent_rows.get())

            if int(self.ent_goal_x.get()) >= rows:
                self.ent_goal_x.delete(0, "end")
                self.ent_goal_x.insert(0, str(rows - 1))
            if int(self.ent_start_x.get()) >= rows:
                self.ent_start_x.delete(0, "end")
                self.ent_start_x.insert(0, str(rows - 1))

        if self.ent_columns.get() == "":
            self.ent_columns.insert(0, "1")
        else:
            columns = int(self.ent_columns.get())

            if int(self.ent_goal_y.get()) >= columns:
                self.ent_goal_y.delete(0, "end")
                self.ent_goal_y.insert(0, str(columns - 1))
            if int(self.ent_start_y.get()) >= columns:
                self.ent_start_y.delete(0, "end")
                self.ent_start_y.insert(0, str(columns - 1))

    def maze_config_changed(self, event) -> None:
        self.btn_search.config(state="disabled")
        self.btn_path.config(state="disabled")
        self.lbl_last_search.config(text="")

    def start_goal_changed(self, event) -> None:
        self.btn_path.config(state="disabled")

    def search_algorithm_changed(self, event) -> None:
        self.btn_path.config(state="disabled")


    ##########################################################################
    #                             Helper Methods                             #
    ##########################################################################

    def show_grid(self, title) -> None:
        """Shows the grid on the screen."""

        image = self.renderer.render(self.grid)
        MazeWindow(parent=self, image=image, title=title)


    ##########################################################################
    #                      Maze Creation and Search Methods                  #
    ##########################################################################

    def generate_maze(self) -> None:
        """Generates a maze using the specified maze algorithm and visualizes it."""

        rows = int(self.ent_rows.get())
        columns = int(self.ent_columns.get())
        self.grid = Grid(rows, columns)  # Create a grid with the specified dimensions.

        maze_algorithm_name = self.var_maze.get()
        maze_algorithm = None

        match maze_algorithm_name:
            case "Binary Tree":
                maze_algorithm = BinaryTree()
            case "Sidewinder":
                maze_algorithm = Sidewinder()
            case "Aldous Broder":
                maze_algorithm = AldousBroder()
            case "Wilson's":
                maze_algorithm = Wilsons()
            case "Hunt and Kill":
                maze_algorithm = HuntAndKill()
            case "Recursive Backtracker":
                maze_algorithm = RecursiveBacktracker()
            case _:
                print("Invalid maze algorithm.")

        # Apply the maze algorithm to the grid:
        if maze_algorithm:
            maze_algorithm.on(self.grid)

        self.show_grid(title=f"Maze - {maze_algorithm_name}")
        self.btn_search.config(state="normal")
        self.lbl_last_search.config(text="")

    def run_search(self) -> None:
        """Applies the specified search algorithm to the maze and visualizes it."""

        start_x = int(self.ent_start_x.get())
        start_y = int(self.ent_start_y.get())
        goal_x = int(self.ent_goal_x.get())
        goal_y = int(self.ent_goal_y.get())
        search_algorithm_name = self.var_search.get()

        self.start = self.grid[start_x, start_y]
        self.goal = self.grid[goal_x, goal_y]

        match search_algorithm_name:
            case "A-star":
                self.distances = astar(self.start, self.goal)
                self.grid.set_distances(self.distances)
            case "Dijkstra":
                self.distances = dijkstra(self.start, self.goal)
                self.grid.set_distances(self.distances)

        self.lbl_last_search.config(text=f"    {search_algorithm_name}")
        self.show_grid(title=f"Search - {search_algorithm_name}")
        self.btn_path.config(state="normal")
        self.search_algorithm_name = search_algorithm_name

    def find_path(self) -> None:
        """Reconstructs the shortest path from the goal to the start and visualizes it."""

        self.distances = self.distances.path_to(self.goal)
        self.grid.set_distances(self.distances)
        self.show_grid(title=f"Path - {self.search_algorithm_name}")


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
