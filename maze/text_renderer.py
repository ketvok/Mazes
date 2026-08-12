class TextRenderer:
    """Renders a grid-based maze as ASCII text."""

    def render(self, grid) -> str:
        """Converts the grid into an ASCII string representation with cells and walls.
        
        Args:
            grid: The grid object to render.
            
        Returns:
            A string containing the ASCII representation of the maze.
        """

        output = "+" + "---+" * grid.columns + "\n"  # Initialize output buffer to be the top boundary of the grid.
        for row in grid.each_row():
            top = "|"  # Bodies and eastern walls for row's cells. Initialize to the western boundary of the row.
            bottom = "+"  # Southern boundaries for row's cells. Initialize to the row's southwest corner.
            for cell in row:
                body = " " + grid.contents_of(cell) + " "
                east_boundary = " " if cell.linked_to(cell.east) else "|"
                top += body + east_boundary
                south_boundary = "   " if cell.linked_to(cell.south) else "---"
                corner = "+"
                bottom += south_boundary + corner
            output += top + "\n"
            output += bottom + "\n"
        return output
