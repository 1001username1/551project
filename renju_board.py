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
        if self._board[row][col] == EMPTY:
            self._board[row][col] = BLACK if is_black else WHITE
            return True
        return False

    def get_board(self):
        return self._board
