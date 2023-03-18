from settings import *
import pygame
import time


class AI:
    def __init__(self, win):
        self.win = win
        self.ai = BLACK

    def is_valid_move(self, row, col):
        if board[row][col] != EMPTY:
            return False
        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if drow == 0 and dcol == 0:
                    continue
                flip_row, flip_col = row + drow, col + dcol
                flipped = False
                while flip_row >= 0 and flip_row < ROWS and flip_col >= 0 and flip_col < COLS:
                    if board[flip_row][flip_col] == EMPTY:
                        break
                    elif board[flip_row][flip_col] == -self.ai:
                        flip_row += drow
                        flip_col += dcol
                        flipped = True
                    else:
                        if flipped:
                            return True
                        break
        return False

    def get_valid_moves(self):
        valid_moves = []
        for row in range(ROWS):
            for col in range(COLS):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def ai_move(self, board):
        max_captured = 0
        best_move = None
        for row, col in self.get_valid_moves():
            captured = 0
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    while 0 <= flip_row < 8 and 0 <= flip_col < 8 and board[flip_row][flip_col] == WHITE:
                        if board[flip_row][flip_col] == EMPTY:
                            break
                        elif board[flip_row][flip_col] == -self.ai:
                            flip_row += drow
                            flip_col += dcol
                            captured += 1
                        else:
                            break

            if captured > max_captured:
                max_captured = captured
                best_move = (row, col)

        if best_move is not None:
            row, col = best_move
            board[row][col] = self.ai
            pygame.draw.circle(self.win, BLACK_COLOR, (
                col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
            pygame.display.update()
            time.sleep(0.3)
            for drow in [-1, 0, 1]:
                for dcol in [-1, 0, 1]:
                    if drow == 0 and dcol == 0:
                        continue
                    flip_row, flip_col = row + drow, col + dcol
                    flipped = False
                    while 0 <= flip_row < ROWS and 0 <= flip_col < COLS:
                        if board[flip_row][flip_col] == EMPTY:
                            break
                        elif board[flip_row][flip_col] == -self.ai:
                            flip_row += drow
                            flip_col += dcol
                            flipped = True
                        else:
                            if flipped:
                                while True:
                                    flip_row -= drow
                                    flip_col -= dcol
                                    board[flip_row][flip_col] = self.ai
                                    pygame.draw.circle(self.win, BLACK_COLOR, (
                                        flip_col*SQUARE_SIZE + SQUARE_SIZE // 2, flip_row*SQUARE_SIZE + SQUARE_SIZE // 2), PIECE_RADIUS)
                                    pygame.display.update()
                                    time.sleep(0.3)
                                    if flip_row == row and flip_col == col:
                                        break
                                break
                            else:
                                break
        return best_move
