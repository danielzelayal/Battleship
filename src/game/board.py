import pygame
from .constants import *

class Board:
    def __init__(self, surface, origin_x, origin_y):
        self.surface = surface
        self.origin_x = origin_x
        self.origin_y = origin_y

    def draw_grid(self):
        for row in range(GRID_SIZE + 1):
            pygame.draw.line(
                self.surface,
                LINE_COLOR,
                (self.origin_x, self.origin_y + row * CELL_SIZE),
                (self.origin_x + GRID_SIZE * CELL_SIZE, self.origin_y + row * CELL_SIZE)
            )
        for col in range(GRID_SIZE + 1):
            pygame.draw.line(
                self.surface,
                LINE_COLOR,
                (self.origin_x + col * CELL_SIZE, self.origin_y),
                (self.origin_x + col * CELL_SIZE, self.origin_y + GRID_SIZE * CELL_SIZE)
            )
