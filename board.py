class Board:
    """Класс дошки."""
    def __init__(self):
        """Дошка зберігається у списку списків."""
        self.board = []

        for i in range(3):
            self.board.append([])

            for y in range(3):
                self.board[i].append('.')
  
    def get_board(self):
        """Отримати дошку у вигляді строки."""
        res = ''

        for i in self.board:
            for y in i:
                res += y + '  '
            
            res += '\n'
        
        return res
