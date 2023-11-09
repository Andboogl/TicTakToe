"""QMessageBox showing."""


from PyQt6.QtWidgets import QMessageBox


def show_message(win, text):
    """Show QMessageBox

    Args:
        win (QMainWindow): Main window
        text (str): QMessageBox text
    """
    message_box = QMessageBox(win)
    message_box.setText(text)
    message_box.exec()
