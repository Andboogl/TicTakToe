from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from design.design import Ui_MainWindow
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import QRect
from board import Board
import figures
import random
import sys


class MainWindow(QMainWindow):
    """Класс, який створює вікно программи."""
    def __init__(self):
        """Ініціалізація."""
        QMainWindow.__init__(self)

        self.whose_move = random.choice([0, 1])  # Хто буде ходити першим
        self.board = Board()  # Доска

        # Загружаємо віджети
        self.widgets = Ui_MainWindow()
        self.widgets.setupUi(self)
        
        # Додаємо дії кнопкам
        self.widgets.pushButton.clicked.connect(lambda: self.add_figure(1))
        self.widgets.pushButton_2.clicked.connect(lambda: self.add_figure(2))
        self.widgets.pushButton_3.clicked.connect(lambda: self.add_figure(3))
        self.widgets.pushButton_4.clicked.connect(lambda: self.add_figure(4))
        self.widgets.pushButton_5.clicked.connect(lambda: self.add_figure(5))
        self.widgets.pushButton_6.clicked.connect(lambda: self.add_figure(6))
        self.widgets.pushButton_7.clicked.connect(lambda: self.add_figure(7))
        self.widgets.pushButton_8.clicked.connect(lambda: self.add_figure(8))
        self.widgets.pushButton_9.clicked.connect(lambda: self.add_figure(9))
        self.widgets.create_new_game.triggered.connect(self.create_new_game)
    
    def create_new_game(self):
        """Створити нову гру."""
        self = MainWindow()
        self.show()

    def add_figure(self, btn):
        """Додати фігуру на дошку."""
        buttons = {
            1: [0, 0, 15, 15],
            2: [0, 1, 15, 160],
            3: [1, 0, 170, 20],
            4: [1, 1, 170, 160],
            5: [0, 2, 15, 300],
            6: [1, 2, 170, 300],
            7: [2, 2, 310, 300],
            8: [2, 1, 310, 160],
            9: [2, 0, 310, 20],
        }

        try:
            # Якщо зараз хід хрестика
            if self.whose_move == 0:
                dagger = figures.Dagger(self.board.board, buttons[btn][0], buttons[btn][1])

                pixmap = QPixmap(dagger.IMG_PATH)
        
                label = QLabel(self)
                label.setPixmap(pixmap)
                label.setScaledContents(True)
                label.setGeometry(QRect(buttons[btn][2], buttons[btn][3], 130, 130))
                label.show()

                self.whose_move = 1
            
            # Якщо зараз хід нулика
            else:
                circle = figures.Circle(self.board.board, buttons[btn][0], buttons[btn][1])

                pixmap = QPixmap(circle.IMG_PATH)
        
                label = QLabel(self)
                label.setPixmap(pixmap)
                label.setScaledContents(True)
                label.setGeometry(QRect(buttons[btn][2], buttons[btn][3], 130, 130))
                label.show()
        
                self.whose_move = 0
            
            x = self.checking_for_win()

            if not x:
                self.checking_for_piece()
        
        # Якщо поле вже зайняте
        except figures.NotEmptyError:
            messageBox = QMessageBox(self)
            messageBox.setText('Це поле вже зайняте')
            messageBox.exec()
    
    def circle_win(self):
        """Цей код виповняється, коли кружки виграють."""
        messageBox = QMessageBox(self)
        messageBox.setText('Нулики виграли')
        messageBox.exec() 

    def dagger_win(self):
        """Цей код виповняється, коли кружки виграють."""
        messageBox = QMessageBox(self)
        messageBox.setText('Хрестики виграли')
        messageBox.exec()
    
    def block_buttons(self):
        """Заблокувати кнопки."""
        self.widgets.pushButton.setEnabled(False)
        self.widgets.pushButton_2.setEnabled(False)
        self.widgets.pushButton_3.setEnabled(False)
        self.widgets.pushButton_4.setEnabled(False)
        self.widgets.pushButton_5.setEnabled(False)
        self.widgets.pushButton_6.setEnabled(False)
        self.widgets.pushButton_7.setEnabled(False)
        self.widgets.pushButton_8.setEnabled(False)
        self.widgets.pushButton_9.setEnabled(False)

    def checking_for_piece(self):
        """Перевірка на нічʼю."""
        figures = []
        for i in self.board.board:
            for y in i:
                if y != '.':
                    figures.append(False)
                
                else:
                    figures.append(True)
        
        if not True in figures:
            self.block_buttons()
            messageBox = QMessageBox(self)
            messageBox.setText('Нічия')
            messageBox.exec()

            self = MainWindow()
            self.show()

    def checking_for_win(self):
        """Перевірка на вийгриш."""
        diagonals = (
            [self.board.board[0][0], self.board.board[1][1], self.board.board[2][2]],
            [self.board.board[2][0], self.board.board[1][1], self.board.board[0][2]],
        )

        verticals = (
            # Вертикальні вертикалі
            [self.board.board[0][0], self.board.board[1][0], self.board.board[2][0]],
            [self.board.board[0][1], self.board.board[1][1], self.board.board[2][1]],
            [self.board.board[0][2], self.board.board[1][2], self.board.board[2][2]],

            # Горизонтальні вертикалі
            [self.board.board[0][0], self.board.board[0][1], self.board.board[0][2]],
            [self.board.board[1][0], self.board.board[1][1], self.board.board[1][2]],
            [self.board.board[2][0], self.board.board[2][1], self.board.board[2][2]],
        )

        is_winner = None
        
        # Перевірки на нулик
        # --------------------------------------
        if diagonals[0][0] == 'O' and diagonals[0][1] == 'O' and diagonals[0][2] == 'O':
            is_winner = True
            self.circle_win()
        
        if diagonals[1][0] == 'O' and diagonals[1][1] == 'O' and diagonals[1][2] == 'O':
            is_winner = True
            self.circle_win()
    
        if verticals[0][0] == 'O' and verticals[0][1] == 'O' and verticals[0][2] == 'O':
            is_winner = True
            self.circle_win()
        
        if verticals[1][0] == 'O' and verticals[1][1] == 'O' and verticals[1][2] == 'O':
            is_winner = True
            self.circle_win()
        
        if verticals[2][0] == 'O' and verticals[2][1] == 'O' and verticals[2][2] == 'O':
            is_winner = True
            self.circle_win()
            print('32')
        
        if verticals[3][0] == 'O' and verticals[3][1] == 'O' and verticals[3][2] == 'O':
            is_winner = True
            self.circle_win()
        
        if verticals[4][0] == 'O' and verticals[4][1] == 'O' and verticals[4][2] == 'O':
            is_winner = True
            self.circle_win()
        
        if verticals[5][0] == 'O' and verticals[5][1] == 'O' and verticals[5][2] == 'O':
            is_winner = True
            self.circle_win()
        # --------------------------------------
        
        # Перевірки на хрестик
        # --------------------------------------
        if diagonals[1][0] == '-' and diagonals[1][1] == '-' and diagonals[1][2] == '-':
            is_winner = True
            self.dagger_win()
    
        if diagonals[0][0] == '-' and diagonals[0][1] == '-' and diagonals[0][2] == '-':
            is_winner = True
            messageBox = QMessageBox(self)
            messageBox.setText('Хрестики виграли')
            self.dagger_win()
        
        if verticals[0][0] == '-' and verticals[0][1] == '-' and verticals[0][2] == '-':
            is_winner = True
            self.dagger_win()
        
        if verticals[1][0] == '-' and verticals[1][1] == '-' and verticals[1][2] == '-':
            is_winner = True
            self.dagger_win()
        
        if verticals[2][0] == '-' and verticals[2][1] == '-' and verticals[2][2] == '-':
            is_winner = True
            self.dagger_win()
        
        if verticals[3][0] == '-' and verticals[3][1] == '-' and verticals[3][2] == '-':
            is_winner = True
            self.dagger_win()
        
        if verticals[4][0] == '-' and verticals[4][1] == '-' and verticals[4][2] == '-':
            is_winner = True
            self.dagger_win()
        
        if verticals[5][0] == '-' and verticals[5][1] == '-' and verticals[5][2] == '-':
            is_winner = True
            self.dagger_win()
        # --------------------------------------
    
        # Якщо є переможець
        if is_winner:
            self.block_buttons()

            self = MainWindow()
            self.show()
            return True
        
        return False


def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
