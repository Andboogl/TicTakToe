"""Module to work with figures."""


from api.board import Board


class _BoardObject:
    """Board object."""
    IMG: str  # Object image

    def __init__(self, board: Board, x: int, y: int):
        """Puting the figure on the board

        Args:
            board (Board): Board
            x (int): X-place
            y (int): Y-place
        """
        board.put_figure(x, y, str(self))

    def __str__(self):
        return self.IMG


class Circle(_BoardObject):
    """Circle."""
    IMG = '•'


class Dagger(_BoardObject):
    """Dagger."""
    IMG = '-'
