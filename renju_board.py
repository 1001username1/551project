# Author: Qianyi zhang   qizhang zhu
# Date: 2024.11.22
# Description: To define the boardtable  


from message_box import show_message

EMPTY = 0
BLACK = 1
WHITE = 2


class RenjuBoard:
    def __init__(self):
        self._board = [[EMPTY] * 15 for _ in range(15)]
        self.reset()

    def reset(self):
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15

    def move(self, row, col, is_black):
        if 0 <= row < len(self._board) and 0 <= col < len(self._board[0]):
            if self._board[row][col] == EMPTY:
                self._board[row][col] = BLACK if is_black else WHITE
                return True
            else:
                show_message("This position is already occupied.")
        else:
            show_message("Invalid move: Position out of bounds.")
        return False
        

    def get_board(self):
        return self._board
