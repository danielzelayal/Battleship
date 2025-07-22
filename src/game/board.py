import pygame
from constants import *

def grid(window, SIZE, ROWS):
    #start grid
    #distance between rows
    distanceBtwRows = SIZE // ROWS
    x = 0
    y = 0
    for l in range(ROWS):
        # increase x and y by distance
        x += distanceBtwRows
        y += distanceBtwRows
        #draw grid
        pygame.draw.line(window, (BLACK), (x, 0), (x, SIZE))

        pygame.draw.line(window, (BLACK), (0, y), (SIZE, y))

def redraw(window):
    window.fill((BG_COLOR))
    grid(window, SIZE, ROWS)
    #update display
    pygame.display.update()

def main():
    window = pygame.display.set_mode((SIZE, SIZE))

    play = True

    #main loop
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #redraw function
        redraw(window)
main()