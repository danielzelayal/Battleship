import pygame
from .constants import *

class Board:
    def __init__(self, surface, origin_x, origin_y):
        self.surface = surface
        self.origin_x = origin_x
        self.origin_y = origin_y
        self.selected_cells = set() #set of rows, cols

    def draw_grid(self):
        for (row, col) in self.selected_cells:
            rect = pygame.Rect(
                self.origin_x + col * CELL_SIZE,
                self.origin_y + row * CELL_SIZE,
                CELL_SIZE,
                CELL_SIZE
            )
            pygame.draw.rect(self.surface, GREEN, rect)

        for r in range(GRID_SIZE + 1):
            start = (self.origin_x, self.origin_y + r * CELL_SIZE)
            end   = (self.origin_x + GRID_SIZE * CELL_SIZE, self.origin_y + r * CELL_SIZE)
            pygame.draw.line(self.surface, LINE_COLOR, start, end)
        for c in range(GRID_SIZE + 1):
            start = (self.origin_x + c * CELL_SIZE, self.origin_y)
            end   = (self.origin_x + c * CELL_SIZE, self.origin_y + GRID_SIZE * CELL_SIZE)
            pygame.draw.line(self.surface, LINE_COLOR, start, end)

    def handle_click(self, mouse_pos):
        x, y = mouse_pos
        grid_x = x - self.origin_x
        grid_y = y - self.origin_y

        #print(f"Mouse @ {mouse_pos} -> grid offset ({grid_x},{grid_y})")

        if 0 <= grid_x < GRID_SIZE * CELL_SIZE and 0 <= grid_y < GRID_SIZE * CELL_SIZE:
            col = grid_x // CELL_SIZE
            row = grid_y // CELL_SIZE
            cell = (row, col)

            if cell in self.selected_cells:
                self.selected_cells.remove(cell)
                #print(f"-> unselected {cell}")
            else:
                self.selected_cells.add(cell)
                #print(f"-> selected {cell}")
            #print(f"Clicked cell: {cell}")
