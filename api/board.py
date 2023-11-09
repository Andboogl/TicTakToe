"""Game board."""


from api.__checking_for_win import checking_for_win
from api.__checking_for_piece import checking_for_piece


class FieldError(Exception):
    """FieldError error."""


class Board:
    """Board."""
    def __init__(self):
        """Creating of board."""
        self.board = []

        for i in range(3):
            self.board.append([])

            for _ in range(3):
                self.board[i].append('.')

        self.__moves = []

    def check_for_piece(self):
        """Returns True, if it's piece. Else false."""
        return checking_for_piece(self.board, '•', '-')

    def get_winner(self):
        """
        Get the winner.
        0: Daggers
        1: Circles
        False: Not daggers and not circles
        """
        return checking_for_win(self.board, '•', '-')

    def cancel_move(self):
        """Cancel last move."""
        x = self.__moves[-1][0]
        y = self.__moves[-1][1]
        self.board[x][y] = '.'
        self.__moves.pop()

    def put_figure(self, x, y, figure):
        """Put figure in the board

        Args:
            x (int): X-position
            y (int): Y-position
            figure (str): Figure photo/unicode
        """
        if self.board[x][y] != '.':
            raise FieldError('This field is not empty')

        else:
            self.board[x][y] = str(figure)
            self.__moves.append((x, y))

    def __str__(self):
        result = ''
        for i in self.board:
            for y in i:
                result += y + '  '

            result += '\n'

        return result
