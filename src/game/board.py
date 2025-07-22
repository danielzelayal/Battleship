import pygame
from constants import *

def grid(window, size, rows):
    #start grid
    #distance between rows
    distanceBtwRows = size // rows
    x = 0
    y = 0
    for l in range(rows):
        # increase x and y by distance
        x += distanceBtwRows
        y += distanceBtwRows
        #draw grid
        pygame.draw.line(window, (BLACK), (x, 0), (x, size))

        pygame.draw.line(window, (BLACK), (0, y), (size, y))

def redraw(window):
    global size, rows
    window.fill((BG_COLOR))
    grid(window, size, rows)
    #update display
    pygame.display.update()

def main():
    global size, rows
    size = SIZE
    rows = ROWS
    window = pygame.display.set_mode((size, size))

    play = True

    #main loop
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #redraw function
        redraw(window)
main()