import pygame
from renju_board import EMPTY, BLACK, WHITE

# Define the color
BLACK_COLOR = [0, 0, 0]
WHITE_COLOR = [255, 255, 255]
BACKGROUND_COLOR = [125, 95, 24]


def draw_board(screen, board):
    for h in range(1, 16):
        pygame.draw.line(screen, BLACK_COLOR, [40, h * 40], [600, h * 40], 1)
        pygame.draw.line(screen, BLACK_COLOR, [h * 40, 40], [h * 40, 600], 1)

    pygame.draw.rect(screen, BLACK_COLOR, [36, 36, 568, 568], 3)

    pygame.draw.circle(screen, BLACK_COLOR, [320, 320], 5, 0)
    pygame.draw.circle(screen, BLACK_COLOR, [160, 160], 3, 0)
    pygame.draw.circle(screen, BLACK_COLOR, [160, 480], 3, 0)
    pygame.draw.circle(screen, BLACK_COLOR, [480, 160], 3, 0)
    pygame.draw.circle(screen, BLACK_COLOR, [480, 480], 3, 0)

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != EMPTY:
                color = BLACK_COLOR if board[row][col] == BLACK else WHITE_COLOR
                pos = [40 * (col + 1), 40 * (row + 1)]
                pygame.draw.circle(screen, color, pos, 18, 0)


def draw_buttons(screen):
    pygame.draw.rect(screen, [200, 200, 200], [640, 50, 120, 400])
    pygame.draw.rect(screen, [255, 0, 0], [650, 60, 100, 40])
    font = pygame.font.SysFont(None, 24)
    quit_text = font.render("quit game", True, [255, 255, 255])
    screen.blit(quit_text, (660, 70))
    pygame.draw.rect(screen, [0, 255, 0], [650, 120, 100, 40])
    restart_text = font.render("restart", True, [255, 255, 255])
    screen.blit(restart_text, (660, 130))
    pygame.draw.rect(screen, [0, 0, 255], [650, 180, 100, 40])
    pause_text = font.render("pause", True, [255, 255, 255])
    screen.blit(pause_text, (660, 190))
    pygame.draw.rect(screen, [255, 165, 0], [650, 240, 100, 40])
    color_text = font.render("adjust color", True, [255, 255, 255])
    screen.blit(color_text, (660, 250))


def show_winner(screen, winner):
    font = pygame.font.SysFont(None, 48)
    text = font.render(winner, True, [255, 0, 0])
    screen.blit(text, (200, 300))
