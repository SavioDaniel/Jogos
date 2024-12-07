import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 600, 700  
LINE_WIDTH = 10
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Velha com IA")
FONT = pygame.font.Font(None, 80)
BUTTON_FONT = pygame.font.Font(None, 40)
SCORE_FONT = pygame.font.Font(None, 50)
COLORS = {"bg": (28, 170, 156), "line": (23, 145, 135), "X": (84, 84, 84), "O": (242, 235, 211), "button": (200, 200, 200)}

board = [[" " for _ in range(3)] for _ in range(3)]

CELL_SIZE = WIDTH // 3
PLAYER = "X"
AI = "O"
player_score = 0
ai_score = 0
current_player = PLAYER
start_with_ai = False  

BUTTON_RESTART = pygame.Rect(100, 620, 150, 50)
BUTTON_EXIT = pygame.Rect(350, 620, 150, 50)

def draw_board():
    """Desenha o tabuleiro."""
    SCREEN.fill(COLORS["bg"])
    for i in range(1, 3):
        pygame.draw.line(SCREEN, COLORS["line"], (0, i * CELL_SIZE), (WIDTH, i * CELL_SIZE), LINE_WIDTH)
        pygame.draw.line(SCREEN, COLORS["line"], (i * CELL_SIZE, 0), (i * CELL_SIZE, WIDTH), LINE_WIDTH)

def draw_symbols():
    """Desenha os símbolos no tabuleiro."""
    for row in range(3):
        for col in range(3):
            if board[row][col] == "X":
                text = FONT.render("X", True, COLORS["X"])
                SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))
            elif board[row][col] == "O":
                text = FONT.render("O", True, COLORS["O"])
                SCREEN.blit(text, (col * CELL_SIZE + CELL_SIZE // 3, row * CELL_SIZE + CELL_SIZE // 4))

def draw_buttons():
    """Desenha os botões e o placar."""
    pygame.draw.rect(SCREEN, COLORS["button"], BUTTON_RESTART)
    pygame.draw.rect(SCREEN, COLORS["button"], BUTTON_EXIT)
    restart_text = BUTTON_FONT.render("Reiniciar", True, (0, 0, 0))
    exit_text = BUTTON_FONT.render("Sair", True, (0, 0, 0))
    SCREEN.blit(restart_text, (BUTTON_RESTART.x + 15, BUTTON_RESTART.y + 10))
    SCREEN.blit(exit_text, (BUTTON_EXIT.x + 45, BUTTON_EXIT.y + 10))

    # Placar
    score_text = SCORE_FONT.render(f"Humano: {player_score}  IA: {ai_score}", True, (0, 0, 0))
    SCREEN.blit(score_text, (WIDTH // 4, 550))

def get_winner():
    """Verifica se há um vencedor."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

def is_full():
    """Verifica se o tabuleiro está cheio."""
    return all(board[row][col] != " " for row in range(3) for col in range(3))

def minimax(is_maximizing):
    """Implementa o algoritmo Minimax."""
    winner = get_winner()
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = AI
                    score = minimax(False)
                    board[row][col] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    board[row][col] = PLAYER
                    score = minimax(True)
                    board[row][col] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move():
    """Encontra a melhor jogada para a IA."""
    best_score = -math.inf
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                board[row][col] = AI
                score = minimax(False)
                board[row][col] = " "
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def reset_game():
    """Reinicia o jogo."""
    global board, current_player, start_with_ai
    board = [[" " for _ in range(3)] for _ in range(3)]
    start_with_ai = not start_with_ai  # Alterna quem começa
    current_player = AI if start_with_ai else PLAYER

def main():
    global current_player, player_score, ai_score

    running = True
    while running:
        draw_board()
        draw_symbols()
        draw_buttons()

        winner = get_winner()
        if winner or is_full():
            if winner == PLAYER:
                player_score += 1
            elif winner == AI:
                ai_score += 1
            reset_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()

                if BUTTON_RESTART.collidepoint(x, y):
                    reset_game()
                elif BUTTON_EXIT.collidepoint(x, y):
                    running = False
                elif y < WIDTH and current_player == PLAYER:
                    row, col = y // CELL_SIZE, x // CELL_SIZE
                    if board[row][col] == " ":
                        board[row][col] = PLAYER
                        current_player = AI
            elif current_player == AI:
                pygame.time.wait(500)
                move = best_move()
                if move:
                    board[move[0]][move[1]] = AI
                    current_player = PLAYER

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
