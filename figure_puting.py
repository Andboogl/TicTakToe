"""Figure puting to the board"""


import api
import utils
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QLabel


def put_figure(self, figure_number):
    """Put figure in the board"""
    btns = {
        1: {'place_on_board': [0, 0], 'place_on_window': [60, 60]},
        2: {'place_on_board': [0, 1], 'place_on_window': [220, 60]},
        3: {'place_on_board': [0, 2], 'place_on_window': [370, 60]},
        4: {'place_on_board': [1, 0], 'place_on_window': [70, 210]},
        5: {'place_on_board': [1, 1], 'place_on_window': [220, 210]},
        6: {'place_on_board': [1, 2], 'place_on_window': [370, 210]},
        7: {'place_on_board': [2, 0], 'place_on_window': [60, 340]},
        8: {'place_on_board': [2, 1], 'place_on_window': [220, 340]},
        9: {'place_on_board': [2, 2], 'place_on_window': [370, 340]}
    }

    try:
        if self.whose_move == 0:
            api.Dagger(
                self.board,
                btns[figure_number]['place_on_board'][0],
                btns[figure_number]['place_on_board'][1]
            )

            pixmap = QPixmap('img/dagger.png')

            dagger_image = QLabel(self)
            dagger_image.setScaledContents(True)
            dagger_image.setGeometry(
                btns[figure_number]['place_on_window'][0],
                btns[figure_number]['place_on_window'][1],
                120,
                120,
            )
            dagger_image.setPixmap(pixmap)
            dagger_image.show()

            self.moves.append(dagger_image)
            self.whose_move = 1

        elif self.whose_move == 1:
            api.Circle(
                self.board,
                btns[figure_number]['place_on_board'][0],
                btns[figure_number]['place_on_board'][1]
            )

            pixmap = QPixmap('img/circle.png')

            circle_image = QLabel(self)
            circle_image.setScaledContents(True)
            circle_image.setGeometry(
                btns[figure_number]['place_on_window'][0],
                btns[figure_number]['place_on_window'][1],
                120,
                120,
            )
            circle_image.setPixmap(pixmap)
            circle_image.show()

            self.moves.append(circle_image)
            self.whose_move = 0

        winner = self.board.get_winner()

        if winner == '-':
            utils.show_message(self, 'Хрестики вийграли')
            self.block_interface()
            self.new_game()

        elif winner == '•':
            utils.show_message(self, 'Нулики вийграли')
            self.block_interface()
            self.new_game()

        else:
            is_piece = self.board.check_for_piece()

            if is_piece:
                utils.show_message(self, 'Нічия')
                self.block_interface()
                self.new_game()

    except api.FieldError:
        x = 'хрестиками' if self.whose_move == 1 else 'нуликами'
        utils.show_message(self, f'Це поле вже зайняте {x}')
