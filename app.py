"""Module create main window and process user actions."""


import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
import api
from design.main_window import Ui_MainWindow
from figure_puting import put_figure
import utils


class MainWindow(QMainWindow):
    """Class create main window of app."""
    def __init__(self):
        QMainWindow.__init__(self)

        self.whose_move = random.choice([0, 1])

        self.setFixedSize(537, 492)  # Window fixed size
        self.setWindowTitle('TikTakToe 2.0')  # Window title

        # Design loading
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)

        # Board loading
        self.board = api.Board()

        # Processing buttons click
        self.widgets.btn1.clicked.connect(lambda: put_figure(self, 1))
        self.widgets.btn2.clicked.connect(lambda: put_figure(self, 2))
        self.widgets.btn3.clicked.connect(lambda: put_figure(self, 3))
        self.widgets.btn4.clicked.connect(lambda: put_figure(self, 4))
        self.widgets.btn5.clicked.connect(lambda: put_figure(self, 5))
        self.widgets.btn6.clicked.connect(lambda: put_figure(self, 6))
        self.widgets.btn7.clicked.connect(lambda: put_figure(self, 7))
        self.widgets.btn8.clicked.connect(lambda: put_figure(self, 8))
        self.widgets.btn9.clicked.connect(lambda: put_figure(self, 9))
        self.widgets.new_game.triggered.connect(self.new_game)
        self.widgets.cancel_move.triggered.connect(self.cancel_move)
        self.widgets.close_app.triggered.connect(exit)

        self.moves = []

    def block_interface(self):
        """Block buttons to put figure and button cancel move."""
        self.widgets.btn1.setEnabled(False)
        self.widgets.btn2.setEnabled(False)
        self.widgets.btn3.setEnabled(False)
        self.widgets.btn4.setEnabled(False)
        self.widgets.btn5.setEnabled(False)
        self.widgets.btn6.setEnabled(False)
        self.widgets.btn7.setEnabled(False)
        self.widgets.btn8.setEnabled(False)
        self.widgets.btn9.setEnabled(False)

        self.widgets.cancel_move.setEnabled(False)  # Cancel move btn

    def cancel_move(self):
        """Cancel user move."""
        try:
            self.board.cancel_move()
            self.moves[-1].hide()
            self.moves.pop()

        except IndexError:
            utils.show_message(self, 'Ви не зробили хід для скасування')

    def new_game(self):
        """Create new game window."""
        win = MainWindow()
        win.show()


def start_app():
    """App starting."""
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
