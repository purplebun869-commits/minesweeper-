import pygame
import random

ROWS = 100
COLS = 100
MINES = 300
CELL_SIZE = 8
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

#purple yayyyyy

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
visible = [[False for _ in range(COLS)] for _ in range(ROWS)]
flagged = [[False for _ in range(COLS)] for _ in range(ROWS)]

def place_mine():
    count = 0
    while count < MINES:
        r = random.randint(0, ROWS-1)
        c = random.randint(0, COLS-1)
        if board[r][c] != "M":
            board[r][c] = "M"
            count +=1

def count_mines(r, c):
    dirs = [(-1, -1), (-1,0), (-1,-1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
    ct = 0
    