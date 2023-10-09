# Import necessary libraries
import numpy as np
import pygame
import sys
from CONSTANTS import *

# Initialize Pygame
pygame.init()

# Initialize game variables
player = 1
game_over = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create the game window
pygame.display.set_caption("TIC TAC TOE")
screen.fill(BG_COLOR)

# Create the game board using NumPy
board = np.zeros((BOARD_ROW, BOARD_COLS))


# Draw the game board grid lines
def draw_lines():
    # 1ST HORIZONTAL LINE
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    # 2ST HORIZONTAL LINE
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # 1ST VERTICAL LINE
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2ST VERTICAL LINE
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)


# Draw X and O figures on the board
def draw_figure():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, C_COLOR,
                                   (int(col * SQUARE_SIZE + SQUARE_SIZE / 2), int(row * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   CIRCLE_RADIUS,
                                   CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE),
                                 (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 CROSS_WIDTH)


# Mark a square on the board with a player's mark
def mark_square(row, col, p):
    board[row][col] = p


# Check if a square on the board is available for marking
def available_square(row, col):
    return board[row][col] == 0
    # if board[row][col] == 0:
    #     return True
    # else:return False


# Check if the game board is full
def is_board_full():
    for row in range(BOARD_ROW):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True


# Check for a win condition
def check_win(p):
    # Code to check vertical, horizontal, and diagonal win conditions
    for col in range(BOARD_COLS):
        if board[0][col] == p and board[1][col] == p and board[2][col] == p:
            draw_vertical_winning_line(col, p)
            return True
    # horizontal win
    for row in range(BOARD_ROW):
        if board[row][0] == p and board[row][1] == p and board[row][2] == p:
            draw_horizontal_winning_line(row, p)
            return True
    # asc diagonal win
    if board[2][0] == p and board[1][1] == p and board[0][2] == p:
        draw_asc_diagonal(p)
        return True
    # desc diagonal win
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        draw_desc_diagonal(p)
        return True

    return False


# Draw a winning vertical line
def draw_vertical_winning_line(col, p):
    pos_x = col * SQUARE_SIZE + SQUARE_SIZE / 2
    color = None  # Default color value
    if p == 1:
        color = C_COLOR
    elif p == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (pos_x, 15), (pos_x, HEIGHT - 15), 15)


# Draw a winning horizontal line
def draw_horizontal_winning_line(row, p):
    pos_y = row * SQUARE_SIZE * SQUARE_SIZE / 2
    color = None  # Default color value
    if p == 1:
        color = C_COLOR
    elif p == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, pos_y), (WIDTH - 15, pos_y), 15)


# Draw an ascending diagonal winning line
def draw_asc_diagonal(p):
    color = None  # Default color value
    if p == 1:
        color = C_COLOR
    elif p == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15)


# Draw a descending diagonal winning line
def draw_desc_diagonal(p):
    color = None  # Default color value
    if p == 1:
        color = C_COLOR
    elif p == 2:
        color = X_COLOR
    pygame.draw.line(screen, color, (15, 15), (HEIGHT - 15, WIDTH - 15), 15)


# Restart the game
def restart():
    global player, game_over
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    game_over = False
    for row in range(BOARD_ROW):
        for col in range(BOARD_COLS):
            board[row][col] = 0


def maingame():
    # Draw initial game board lines
    global game_over, player
    draw_lines()

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                Mouse_x = event.pos[0]  # x
                Mouse_y = event.pos[1]  # x

                clicked_row = int(Mouse_y // SQUARE_SIZE)
                clicked_col = int(Mouse_x // SQUARE_SIZE)
                if available_square(clicked_row, clicked_col):
                    mark_square(clicked_row, clicked_col, player)
                    if check_win(player):
                        game_over = True
                    player = player % 2 + 1
                    # if player == 1:
                    #     mark_square(clicked_row, clicked_col, 1)
                    #     if check_win(player):
                    #         game_over = True
                    #     player = 2
                    # elif player == 2:
                    #     mark_square(clicked_row, clicked_col, 2)
                    #     if check_win(player):
                    #         game_over = True
                    #     player = 1
                    draw_figure()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart()
        # Update the display
        pygame.display.update()


if __name__ == "__main__":
    maingame()
