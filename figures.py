"""Модуль з фігурами."""


class NotEmptyError(Exception): ...


class Figure:
    """Класс, який відповідає за кожну фігуру на дошці."""
    IMG_PATH = ...  # Шлях до фотки фігури

    def __init__(self, board, x, y):
        """Ініціалізація."""
        if board[y][x] == '.':
            board[y][x] = str(self)

        else:
            raise NotEmptyError('This value is not empty')


class Circle(Figure):
    """Класс круга."""
    IMG_PATH = 'img/circle.png'
    
    def __repr__(self) -> str:
        return 'O'


class Dagger(Figure):
    """Класс хрестика."""
    IMG_PATH = 'img/dagger.png'

    def __repr__(self) -> str:
        return '-'
