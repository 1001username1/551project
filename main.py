import pygame
from renju_board import RenjuBoard, BLACK, WHITE
from gui import draw_board, draw_buttons, show_winner, BACKGROUND_COLOR
from winner_checker import winner_checker


def is_win(board):
    for row in range(15):
        flag = 0
        for col in range(15):
            if board[row][col] == BLACK:
                flag += 1
                if flag == 5:
                    return "black wins"
            else:
                flag = 0
        flag = 0
        for col in range(15):
            if board[row][col] == WHITE:
                flag += 1
                if flag == 5:
                    return "white wins"
            else:
                flag = 0
    return None


def handle_buttons(event, board, screen, is_paused):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos

        if 650 <= x <= 750 and 60 <= y <= 100:
            pygame.quit()
            exit()

        if 650 <= x <= 750 and 120 <= y <= 160:
            board.reset()
            screen.fill(BACKGROUND_COLOR)
            draw_board(screen, board.get_board())
            pygame.display.flip()

        if 650 <= x <= 750 and 180 <= y <= 220:
            return not is_paused

        if 650 <= x <= 750 and 240 <= y <= 280:
            change_color()
    return is_paused


def change_color():
    global BACKGROUND_COLOR
    BACKGROUND_COLOR = [50, 50, 50] if BACKGROUND_COLOR == [125, 95, 24] else [125, 95, 24]


def main():
    board = RenjuBoard()
    win_checker = winner_checker(board)
    is_black = True
    is_paused = False

    pygame.init()
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("wuziqi")
    screen.fill(BACKGROUND_COLOR)
    draw_board(screen, board.get_board())
    pygame.display.flip()

    running = True
    winner = None

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            is_paused = handle_buttons(event, board, screen, is_paused)

            if is_paused or winner:
                continue

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                if x < 640:
                    row = round((y - 40) / 40)
                    col = round((x - 40) / 40)
                    if board.move(row, col, is_black):
                        is_black = not is_black
                        screen.fill(BACKGROUND_COLOR)
                        draw_board(screen, board.get_board())
                        pygame.display.flip()

                        winner = win_checker.check_winner()
                        if winner:
                            screen.fill(BACKGROUND_COLOR)
                            draw_board(screen, board.get_board())
                            show_winner(screen, winner)
                            pygame.display.flip()

        draw_buttons(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
