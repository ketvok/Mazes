from random import choice, randint
from maze.grid import Grid


class Sidewinder(object):
    """
    Sidewinder algorithm for maze generation.

    Mazes it creates have one unbroken corridor along the northern border.
    """

    def on(self, grid: Grid) -> None:
        for row in grid.each_row():
            run = []
            for cell in row:
                run.append(cell)

                # Check to see if cell is at the eastern or the northern boundary
                at_eastern_boundary = cell.east is None
                at_northern_boundary = cell.north is None

                # 0 == heads; 1 == tails. Heads means "close out the run". Tails means "carve east".
                should_close_out = at_eastern_boundary or (not at_northern_boundary and randint(0, 1) == 0)

                if should_close_out:
                    member = choice(run)  # Pick a random cell from the run.
                    if member.north:
                        member.link(member.north)  # Link picked cell to its northern neighbor.
                    run.clear()
                else:
                    cell.link(cell.east)  # Link cell to its eastern neighbor.
