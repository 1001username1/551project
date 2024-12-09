# Author: Qianyi zhang   qizhang zhu
# Date: 2024.11.30
# Description: Main func, also need to update the information of win、lose



from player_manager import PlayerManager
from login import LoginPage
from renju_board import RenjuBoard
from gui import draw_board, draw_buttons, show_winner, BACKGROUND_COLOR
from winner_checker import winner_checker
import pygame


    

def main():
    player_manager = PlayerManager()

    # show login userinterface
    import tkinter as tk
    root = tk.Tk()
    login_app = LoginPage(root)
    root.mainloop()

    # get player
    player1, player2 = login_app.selected_players
    if not player1 or not player2:
        print("Game aborted: Players not selected.")
        return

    # board initalize
    board = RenjuBoard()
    win_checker = winner_checker(board)
    is_black = True

    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    screen.fill(BACKGROUND_COLOR)
    draw_board(screen, board.get_board())
    pygame.display.flip()

    winner = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos


                if 650 <= x <= 750 and 60 <= y <= 100:
                    pygame.quit()
                    exit()
                if 650 <= x <= 750 and 120 <= y <= 160:
                    board.reset()
                    screen.fill(BACKGROUND_COLOR)
                    draw_board(screen, board.get_board())
                    pygame.display.flip()
                    is_black=True
                  
                if x < 640:
                    row = round((y - 40) / 40)
                    col = round((x - 40) / 40)
                    if board.move(row, col, is_black):
                        is_black = not is_black
                        draw_board(screen, board.get_board())
                        pygame.display.flip()

                        winner = win_checker.check_winner()
                        if winner:
                            draw_board(screen, board.get_board())
                            show_winner(screen, f"{winner} wins!")
                            running =  False

        draw_buttons(screen)
        pygame.display.flip()

    if winner:
        if winner == "Black win":
            player_manager.update_score(player1, "win")
            player_manager.update_score(player2, "loss")
        elif winner == "White win":
            player_manager.update_score(player2, "win")
            player_manager.update_score(player1, "loss")


    pygame.quit()

    main()


if __name__ == "__main__":
    main()
