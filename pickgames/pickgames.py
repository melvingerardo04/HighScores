import pygame
import sys

from pygame import mixer
from pickgames.checkers import index as checkers
from pickgames.tetris import mode
from pickgames.tetris import difficulties
from pickgames.snakes import index
from pickgames.stickman import index as stickman



def pick_games(name):
    display = pygame.display.set_mode([360, 720])
    base_font = pygame.font.SysFont("Calibri", 35, True, False)

    snake_rect = pygame.Rect(80, 200, 200, 50)
    tetris_rect = pygame.Rect(80, 280, 200, 50)
    stickman_rect = pygame.Rect(80, 360, 200, 50)
    checkers_rect = pygame.Rect(80, 440, 200, 50)

    snake_color = pygame.Color('lightskyblue3')
    tetris_color = pygame.Color('lightskyblue3')
    stickman_color = pygame.Color('lightskyblue3')
    checkers_color = pygame.Color('lightskyblue3')
    width = display.get_width()
    height = display.get_height()

    start_game = True
    while start_game:
        display.fill((255, 255, 255))
        pygame.draw.rect(display, snake_color, snake_rect)
        pygame.draw.rect(display, tetris_color, tetris_rect)
        # pygame.draw.rect(display, stickman_color, stickman_rect)
        pygame.draw.rect(display, checkers_color, stickman_rect)

        # text for snakes
        snake_text = base_font.render("Snake", True, (255, 255, 255))
        display.blit(snake_text, (snake_rect.x + 55, snake_rect.y + 10))

        # text for tetris
        tetris_text = base_font.render("Tetris", True, (255, 255, 255))
        display.blit(tetris_text, (tetris_rect.x + 55, tetris_rect.y + 10))

        # text for stickman
        # stickman_text = base_font.render("Stickman", True, (255, 255, 255))
        # display.blit(stickman_text, (stickman_rect.x + 30, stickman_rect.y + 10))

        # text for stickman
        checkers_text = base_font.render("Checkers", True, (255, 255, 255))
        display.blit(checkers_text, (stickman_rect.x + 30, stickman_rect.y + 10))

        mouse_cursor = pygame.mouse.get_pos()
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_ESCAPE:
                    start_game = False
            if width - 280 <= mouse_cursor[0] <= width - 60 and height - 520 <= mouse_cursor[1] <= height - 470:
                snake_color = pygame.Color('lightskyblue4')
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    index.gameLoop(name)
            else:
                snake_color = pygame.Color('lightskyblue3')

            # for Tetris
            if width - 280 <= mouse_cursor[0] <= width - 60 and height - 440 <= mouse_cursor[1] <= height - 390:
                tetris_color = pygame.Color('lightskyblue4')
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    mode.pickMode(name)
                    # difficulties.pickdifficulty(name)
            else:
                tetris_color = pygame.Color('lightskyblue3')

            # for stickman
            # if width - 280 <= mouse_cursor [0] <= width - 60 and height - 360 <= mouse_cursor [1] <= height - 310:
            #     stickman_color = pygame.Color('lightskyblue4')
            #     if eve.type == pygame.MOUSEBUTTONDOWN:
            #         mixer.music.load('Sounds/click.mp3')
            #         mixer.music.play()
            #         stickman.start()
            # else:
            #     stickman_color = pygame.Color('lightskyblue3')

            # for checkers
            if width - 280 <= mouse_cursor[0] <= width - 60 and height - 360 <= mouse_cursor[1] <= height - 310:
                checkers_color = pygame.Color('lightskyblue4')
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    checkers.main(name)

            else:
                checkers_color = pygame.Color('lightskyblue3')
        pygame.display.update()
    else:
        import menu
        menu.menu()


