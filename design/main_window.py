# Form implementation generated from reading ui file 'design/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 492)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.field = QtWidgets.QLabel(parent=self.centralwidget)
        self.field.setGeometry(QtCore.QRect(-20, -10, 561, 501))
        self.field.setText("")
        self.field.setPixmap(QtGui.QPixmap("img/field.png"))
        self.field.setScaledContents(True)
        self.field.setObjectName("field")
        self.btn1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(60, 60, 141, 131))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn1.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(220, 60, 131, 121))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn2.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(370, 60, 131, 121))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn3.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(370, 210, 121, 111))
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn6.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(220, 210, 121, 111))
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn5.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(70, 210, 121, 111))
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn4.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.btn7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(60, 340, 121, 111))
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn7.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(220, 340, 121, 111))
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn8.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(370, 340, 121, 111))
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.btn9.setStyleSheet("background: #FFFFFF;\n"
"border: None;")
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.createMenuBar(MainWindow)

    def createMenuBar(self, MainWindow):
        menuBar = QtWidgets.QMenuBar(MainWindow)
        game_menu = QtWidgets.QMenu('&Гра', MainWindow)
        menuBar.addMenu(game_menu)

        self.new_game = QtGui.QAction('Нова...', MainWindow)
        self.new_game.setShortcut(QtGui.QKeySequence('Ctrl+n'))
        
        self.cancel_move = QtGui.QAction('Скасувати хід...')
        self.cancel_move.setShortcut(QtGui.QKeySequence('Ctrl+z'))

        self.close_app = QtGui.QAction('Вийти з TikTakToe 2.0')
        self.close_app.setShortcut(QtGui.QKeySequence('Ctrl+q'))
        
        game_menu.addAction(self.new_game)
        game_menu.addAction(self.cancel_move)
        game_menu.addAction(self.close_app)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
