# Author: Qianyi zhang   qizhang zhu
# Date: 2024.11.28
# Description: Pytest combinations for checking if the program can run as its supposed to


from unittest.mock import patch
from renju_board import RenjuBoard, BLACK, WHITE
from winner_checker import winner_checker

def test_board_initialization():
    """test initial board"""
    board = RenjuBoard()
    assert len(board._board) == 15
    assert len(board._board[0]) == 15
    assert all(cell == 0 for row in board._board for cell in row)  # Check if all chess pieces are empty

def test_valid_move():
    """Testing effective drop operations"""
    board = RenjuBoard()
    assert board.move(7, 7, is_black=True)  # black move
    assert board._board[7][7] == BLACK

# avoid tkinter message box
@patch("tkinter.messagebox.showinfo")
def test_move_out_of_bounds(mock_messagebox):
    """Test out-of-bounds moves"""
    board = RenjuBoard()
    assert not board.move(-1, 7, is_black=True)  # row out of bounds
    assert not board.move(7, 15, is_black=True)  # column out of bounds
    assert not board.move(20, 20, is_black=True)  # row and column out of bounds

    # message box use times
    assert mock_messagebox.call_count == 3

    # Validate the parameters of each call
    expected_calls = [
        ('Notification', 'Invalid move: Position out of bounds.'),
        ('Notification', 'Invalid move: Position out of bounds.'),
        ('Notification', 'Invalid move: Position out of bounds.'),
    ]
    actual_calls = [call.args for call in mock_messagebox.call_args_list]
    assert actual_calls == expected_calls

@patch("tkinter.messagebox.showinfo")
def test_move_on_occupied_position(mock_messagebox):
    """Test a move in an occupied position"""
    board = RenjuBoard()
    board.move(7, 7, is_black=True)  # black move
    assert not board.move(7, 7, is_black=False)  # White tries to make a move in the same position
    assert board._board[7][7] == BLACK  # The position should remain black
    mock_messagebox.assert_called_once_with("Notification", "This position is already occupied.")

def test_multiple_moves():
    """Test multiple moves"""
    board = RenjuBoard()
    assert board.move(7, 7, is_black=True)  # black move
    assert board.move(7, 8, is_black=False)  # white move
    assert board.move(7, 9, is_black=True)  # black move
    assert board._board[7][7] == BLACK
    assert board._board[7][8] == WHITE
    assert board._board[7][9] == BLACK


# test winner checker
def test_no_winner_initially():
    """There is no winner in the initial state of the test"""
    board = RenjuBoard()
    checker = winner_checker(board)
    assert checker.check_winner() is None

def test_horizontal_win():
    """Test row winner"""
    board = RenjuBoard()
    for col in range(5):
        board.move(7, col, is_black=True)
    checker = winner_checker(board)
    assert checker.check_winner() == "Black win"

def test_vertical_win():
    """Test coloumn winner"""
    board = RenjuBoard()
    for row in range(5):
        board.move(row, 7, is_black=False)
    checker = winner_checker(board)
    assert checker.check_winner() == "White win"

def test_no_winner_with_gaps():
    """There is no winner when testing interval moves"""
    board = RenjuBoard()
    board.move(7, 0, is_black=True)
    board.move(7, 2, is_black=True)
    board.move(7, 4, is_black=True)
    checker = winner_checker(board)
    assert checker.check_winner() is None
