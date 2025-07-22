import pygame
from constants import *

#class Board

def grid(window, SIZE, ROWS):
    #start grid
    #distance between rows or size of our cubes
    distanceBtwRows = SIZE // ROWS
    x = 0
    y = 0
    for l in range(ROWS):
        # increase x and y by distance
        x += distanceBtwRows
        y += distanceBtwRows
        #draw grid
        #line takes two 4 arguments
        #1 and 2, 1 where we will draw (on window) and 2 which color
        #3 - where we will draw again but in what place, on x and 0 by y
        #4 - size of our line, from x until size of our window
        pygame.draw.line(window, (BLACK), (x, 0), (x, SIZE))
        #4 - size of our line, from size of our window until y
        pygame.draw.line(window, (BLACK), (0, y), (SIZE, y))

def redraw(window):
    #fill window with color
    window.fill((BG_COLOR))
    grid(window, SIZE, ROWS)
    #update display
    pygame.display.update()

def main():
    window = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption("AI Battleship")

    play = True

    #main loop
    while play:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #redraw function
        redraw(window)
main()