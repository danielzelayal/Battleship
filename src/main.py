import pygame
from game.constants import *
from game.board import Board

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("AI Battleship")
    clock = pygame.time.Clock()
    board = Board(screen, BOARD_PADDING, BOARD_PADDING)

    running = True
    while running:
        screen.fill(BG_COLOR)
        board.draw_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                board.handle_click(event.pos)

        screen.fill(BG_COLOR)
        board.draw_grid()
        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
