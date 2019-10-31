def winning_diagonal_top_left_to_bottom_right(board, type):
    return board[0][0] == type and board[2][2] == type


def winning_diagonal_bottom_left_to_top_right(board, type):
    return board[2][0] == type and board[0][2] == type


def winning_horizontal_thru_middle(board, type):
    return board[1][0] == type and board[1][2] == type


def winning_vertical_thru_middle(board, type):
    return board[0][1] == type and board[2][1] == type


def winning_top_horizontal(board):
    return board[0][0] == board[0][1] and board[0][0] == board[0][2]


def winning_right_vertical(board):
    return board[0][0] == board[1][0] and board[0][0] == board[2][0]


def winning_bottom_horizontal(board):
    return board[2][0] == board[2][1] and board[2][0] == board[2][2]


def winning_left_vertical(board):
    return board[0][2] == board[1][2] and board[0][2] == board[2][2]


def ticTacToeWinner(board):
    """
    :param board: 2d array of strings 'X', 'O', or '_'
    :return: 'X', 'O', or '_'
    """
    middle = board[1][1]
    if middle != '_' and (winning_diagonal_top_left_to_bottom_right(board, middle) or \
            winning_diagonal_bottom_left_to_top_right(board, middle) or \
            winning_horizontal_thru_middle(board, middle) or \
            winning_vertical_thru_middle(board, middle)):
        return middle
    elif board[0][0] != '_' and (winning_top_horizontal(board) or winning_left_vertical(board)):
        return board[0][0]
    elif board[2][2] != '_' and (winning_right_vertical(board) or winning_bottom_horizontal(board)):
        return board[2][2]
    else:
        return '_'


if __name__ == "__main__":
    board = [['X', '_', '_'],
             ['_', 'X', '_'],
             ['_', '_', 'X']]
    print(ticTacToeWinner(board)) # 'X'
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['O', 'O', 'O']]
    print(ticTacToeWinner(board)) # 'O'