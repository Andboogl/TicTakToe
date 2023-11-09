"""Module to get winner use board."""


def checking_for_win(board_mas, circle, dagger):
    """Return 0, if daggers wins. Return 1, if circles wins. Else return False

    Args:
        board_mas (list): Board
        circle (str): Circle string unicode
        dagger (str): Dagger string unicode
    """

    verticals = (  # Verticals
        (board_mas[0][0], board_mas[0][1], board_mas[0][2]),
        (board_mas[1][0], board_mas[1][1], board_mas[1][2]),
        (board_mas[2][0], board_mas[2][1], board_mas[2][2]),

        (board_mas[0][0], board_mas[1][0], board_mas[2][0]),
        (board_mas[0][1], board_mas[1][1], board_mas[2][1]),
        (board_mas[0][2], board_mas[1][2], board_mas[2][2]),
    )

    diagonals = (  # Diagonals
        (board_mas[0][0], board_mas[1][1], board_mas[2][2]),
        (board_mas[0][2], board_mas[1][1], board_mas[2][0]),
    )

    # Checking circle
    # ------------------------------------
    if verticals[0][0] == circle and verticals[0][1] == circle and verticals[0][2] == circle:
        return circle

    elif verticals[1][0] == circle and verticals[1][1] == circle and verticals[1][2] == circle:
        return circle

    elif verticals[2][0] == circle and verticals[2][1] == circle and verticals[2][2] == circle:
        return circle

    elif verticals[3][0] == circle and verticals[3][1] == circle and verticals[3][2] == circle:
        return circle

    elif verticals[4][0] == circle and verticals[4][1] == circle and verticals[4][2] == circle:
        return circle

    elif verticals[5][0] == circle and verticals[5][1] == circle and verticals[5][2] == circle:
        return circle

    elif diagonals[0][0] == circle and diagonals[0][1] == circle and diagonals[0][2] == circle:
        return circle

    elif diagonals[1][0] == circle and diagonals[1][1] == circle and diagonals[1][2] == circle:
        return circle
    # ------------------------------------

    # Checking dagger
    # ------------------------------------
    elif verticals[0][0] == dagger and verticals[0][1] == dagger and verticals[0][2] == dagger:
        return dagger

    elif verticals[1][0] == dagger and verticals[1][1] == dagger and verticals[1][2] == dagger:
        return dagger

    elif verticals[2][0] == dagger and verticals[2][1] == dagger and verticals[2][2] == dagger:
        return dagger

    elif verticals[3][0] == dagger and verticals[3][1] == dagger and verticals[3][2] == dagger:
        return dagger

    elif verticals[4][0] == dagger and verticals[4][1] == dagger and verticals[4][2] == dagger:
        return dagger

    elif verticals[5][0] == dagger and verticals[5][1] == dagger and verticals[5][2] == dagger:
        return dagger

    elif diagonals[0][0] == dagger and diagonals[0][1] == dagger and diagonals[0][2] == dagger:
        return dagger

    elif diagonals[1][0] == dagger and diagonals[1][1] == dagger and diagonals[1][2] == dagger:
        return dagger
    # ------------------------------------

    else:
        return False
