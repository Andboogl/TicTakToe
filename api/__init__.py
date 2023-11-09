"""Api to work with board and figures
class Board:
    def __init__(self) -> None: ...
Creating of board


class Circle(BoardObject): ...
    IMG = •'
Class of circle


class Dagger(BoardObject):
    IMG = '-'
Class of dagger


class FieldError(Exception): ...
Field exception
"""


from api.board import Board
from api.board import FieldError
from api.figures import Circle
from api.figures import Dagger


__all__ = ['Board', 'Circle', 'Dagger', 'FieldError']
