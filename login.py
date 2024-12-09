# Author: Qianyi zhang   qizhangzhu
# Date: 2024.11.29
# Description: The judge func to calculate if black wins or not.



# determine who's winner, always return false, if have a result, then return true
class winner_checker:
    def __init__(self, board):
        self.board = board
        self.size = len(board._board)

    def check_winner(self):
        for player, name in [(1, "Black"), (2, "White")]:
            if (self._check_vertical(player) or
                self._check_horizontal(player) or
                self._check_positive_diagonal(player) or
                self._check_negative_diagonal(player)):
                return f"{name} win"
        return None
#check vertical direction
    def _check_vertical(self, player):
        for n in range(self.size):
            flag = 0
            for row in self.board._board:
                if row[n] == player:
                    flag += 1
                    if flag == 5:
                        return True
                else:
                    flag = 0
        return False
#check the horizontal direction
    def _check_horizontal(self, player):
        for row in self.board._board:
            flag = 0
            for cell in row:
                if cell == player:
                    flag += 1
                    if flag == 5:
                        return True
                else:
                    flag = 0
        return False
#check the          /
#                  /
#                 /
#                /
#               /
#                   direction
    def _check_positive_diagonal(self, player):
        for x in range(self.size * 2 - 1):
            flag = 0
            for i, row in enumerate(self.board._board):
                if 0 <= x - i < self.size and row[x - i] == player:
                    flag += 1
                    if flag == 5:
                        return True
                else:
                    flag = 0
        return False
#check the      \
#                \
#                 \
#                  \
#                   \
#                   direction
    def _check_negative_diagonal(self, player):
        for x in range(-self.size + 1, self.size):
            flag = 0
            for i, row in enumerate(self.board._board):
                if 0 <= x + i < self.size and row[x + i] == player:
                    flag += 1
                    if flag == 5:
                        return True
                else:
                    flag = 0
        return False

    
