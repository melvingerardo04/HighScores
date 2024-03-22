import pygame
from pickgames.tetris import index
import sys
from pickgames import insertname
from pygame import mixer
import pickgames.pickgames as pickgames


def pickdifficulty(name):
    # screen resolution
    res = (720, 720)
    screen = pygame.display.set_mode(res)
    width = screen.get_width()
    height = screen.get_height()
    base_font = pygame.font.SysFont('Calibri', 40, True, False)
    run = True
    while run:
        mouse_cursor = pygame.mouse.get_pos()
        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if width / 10 - 17 <= mouse_cursor[0] <= width / 4 - 5 and height / 2 - 48 <= mouse_cursor[
                    1] <= height / 2 + 66:
                pygame.draw.circle(screen, '#097392', [width / 10 + 45, height / 2 + 10], 60, 0)
                # for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    level = 1
                    screen = pygame.display.set_mode([480, 720])
                    playEasy(level, name)
            else:
                pygame.draw.circle(screen, '#83B4B3', [width / 10 + 45, height / 2 + 10], 60, 0)

            # mouse hover for medium button
            if width / 2 - 80 <= mouse_cursor[0] <= width / 2 + 98 and height / 2 - 20 <= mouse_cursor[
                    1] <= height / 2 + 39:
                pygame.draw.rect(screen, '#097392', [width / 2 - 80, height / 2 - 20, 180, 60])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    level = 3
                    screen = pygame.display.set_mode([480, 720])
                    playMedium(level, name)

            else:
                pygame.draw.rect(screen, '#83B4B3', [width / 2 - 80, height / 2 - 20, 180, 60])

            # mouse hover for hard button
            if width / 2 + 180 <= mouse_cursor [0] <= width - 82 and height / 2 - 20 <= mouse_cursor [
                    1] <= height / 2 + 39:
                pygame.draw.polygon(screen, '#097392', [[590, 280], [520, 400], [660, 400]])
                if event.type == pygame.MOUSEBUTTONDOWN:

                    level = 5
                    screen = pygame.display.set_mode([480, 720])
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    playHard(level, name)
            else:
                pygame.draw.polygon(screen, '#83B4B3', [[590, 280], [520, 400], [660, 400]])

            easy = base_font.render("Easy", True, '#000000')
            medium = base_font.render("Medium", True, '#000000')
            hard = base_font.render("Hard", True, '#000000')

            screen.blit(easy, (width / 10 + 8, height / 2 - 10))
            screen.blit(medium, [width - 420, height / 2 - 10])
            screen.blit(hard, [width - 170, height / 2 - 10])
            pygame.display.update()
    else:
        # game = "Tetris"
        # insertname.insert_name(game)
        pickgames.pick_games(name)
        pygame.display.update()


def playEasy(level, name):
    difficulties = "Easy"
    index.startGame(level, difficulties, name)


def playMedium(level, name):
    difficulties = "Medium"
    index.startGame(level, difficulties, name)


def playHard(level, name):
    difficulties = "Hard"
    index.startGame(level, difficulties, name)
