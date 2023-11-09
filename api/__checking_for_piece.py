"""Checking for piece."""


from api.__checking_for_win import checking_for_win


def checking_for_piece(board_mas, circle, dagger):
    """Return True, if it's piece. Else False

    Args:
        board_mas (list): Board
    """

    fields = []

    for i in board_mas:
        for y in i:
            fields.append(y)

    if '.' in fields:
        return False

    else:
        winner = checking_for_win(board_mas, circle, dagger)

        if winner == circle or winner == dagger:
            return False

        else:
            return True
