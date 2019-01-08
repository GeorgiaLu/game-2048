import sys
import pygame
from game_board import GameBoard
from title_board import TitleBoard
from game_matrix import Direction

def main():
    pygame.init()

    window_width = 960
    window_height = 720
    window_background_color = (250, 248, 239)
    screen = pygame.display.set_mode((window_width, window_height))
    #screen.fill(window_background_color)

    game_board_width =  window_height * 2 / 3;
    game_board = GameBoard(screen, pygame.Rect((window_width - game_board_width) / 2, window_height - game_board_width, game_board_width, game_board_width), 4)
    #game_board.display()

    title_board_width =  window_height * 2 / 3;
    title_board_height =  window_height * 1 / 3;
    title_board = TitleBoard(screen, pygame.Rect((window_width - title_board_width) / 2, 0, title_board_width, title_board_height))
    #title_board.display()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_UP]:
                    game_board.move(Direction.kUp)
                elif keys[pygame.K_DOWN]:
                    game_board.move(Direction.kDown)
                elif keys[pygame.K_LEFT]:
                    game_board.move(Direction.kLeft)
                elif keys[pygame.K_RIGHT]:
                    game_board.move(Direction.kRight)


        screen.fill(window_background_color)
        game_board.display()
        title_board.display()
        pygame.display.update()

if __name__ == '__main__':
    main()
