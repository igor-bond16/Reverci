import pygame
from settings import *
from player import Player
from ai import AI
import time

pygame.init()


class Game:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player_color = WHITE
        self.player = Player(self.win)
        self.ai = AI(self.win)
        self.font = pygame.font.Font(None, 36)

    def game(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = pygame.mouse.get_pos()
                    self.player.make_move(y//SQUARE_SIZE, x//SQUARE_SIZE)
                    time.sleep(1)
                    self.ai.ai_move(board)

            self.win.fill(BOARD_COLOR)
            for row in range(ROWS):
                for col in range(COLS):
                    x = col * SQUARE_SIZE
                    y = row * SQUARE_SIZE
                    pygame.draw.rect(self.win, BLACK_COLOR,
                                     (x, y, SQUARE_SIZE, SQUARE_SIZE), 2)
                    if board[row][col] == BLACK:
                        pygame.draw.circle(
                            self.win, BLACK_COLOR, (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2), PIECE_RADIUS)
                    elif board[row][col] == WHITE:
                        pygame.draw.circle(
                            self.win, WHITE_COLOR, (x + SQUARE_SIZE // 2, y + SQUARE_SIZE // 2), PIECE_RADIUS)

            for y, x in self.player.get_valid_moves():
                pygame.draw.circle(self.win, DARKGRAY, (x*SQUARE_SIZE + SQUARE_SIZE //
                                   2, y*SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS-20)

            if self.is_game_over(board):
                player = sum(row.count(WHITE) for row in board)
                The_AI = sum(row.count(BLACK) for row in board)
                resolt = self.font.render(
                    f"PLAYER(WHITE): {player} , AI(BLACK): {The_AI}", True, (255, 0, 0))
                if player > The_AI:
                    winner = 'PLAYER'
                else:
                    winner = "AI"
                game_winner = self.font.render(
                    f"The winner is {winner}", True, (255, 0, 0))

                self.win.blit(resolt, (200, 200))
                self.win.blit(game_winner, (200, 400))

            pygame.display.flip()

    def is_game_over(self, board):
        # Check if no more valid moves can be made
        if not any(self.player.is_valid_move(y, x) for x in range(8) for y in range(8)):
            return True
        # Check if the board is full
        if sum(1 for row in board for square in row if square != EMPTY) == 64:
            return True
        return False


if __name__ == '__main__':
    game = Game()
    game.game()
