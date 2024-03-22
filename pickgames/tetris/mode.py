
import pygame
import sys
from pickgames.tetris import twoplayer
from pickgames.tetris import index
import pickgames.pickgames  as pickgames
clock = pygame.time.Clock()
fps = 120


def pickMode(name):
    pickPlayer = True

    pygame.display.set_caption("Created By Melvs")
    # defining a font
    font = pygame.font.SysFont("Calibri", 30, True, False)

    onePlayer = font.render("One Player", True, '#FFFFFF')
    twoPlayer = font.render("Two Player", True, '#FFFFFF')

    one_rect = pygame.Rect(90, 380, 200, 50)
    one_color = pygame.Color('lightskyblue3')

    two_rect = pygame.Rect(90, 440, 200, 50)
    two_color = pygame.Color('lightskyblue3')
    screen = pygame.display.set_mode([360, 720])
    while pickPlayer:
        clock.tick(fps)
        screen.fill((255, 255, 255))
        mouse = pygame.mouse.get_pos()
        get_one_butt_pos = one_rect.x <= mouse [0] <= one_rect.x + 200 and one_rect.y <= mouse [
            1] <= one_rect.y + 50
        get_two_butt_pos = two_rect.x <= mouse [0] <= two_rect.x + 200 and two_rect.y <= mouse [
            1] <= two_rect.y + 50

        pygame.draw.rect(screen, one_color, one_rect)
        pygame.draw.rect(screen, two_color, two_rect)

        screen.blit(onePlayer, (one_rect.x + 35, one_rect.y + 10))
        screen.blit(twoPlayer, (two_rect.x + 30, two_rect.y + 10))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pickPlayer = False
            if get_one_butt_pos:
                one_color = pygame.Color('lightskyblue4')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    index.startGame(1, "Easy", name)
                    # mixer.music.load('Sounds/click.mp3')
                    # mixer.music.play()
                    # pick.pick_games()
                    # insertname.insert_name()
            else:
                one_color = pygame.Color('lightskyblue3')

                # hover for quit button
            if get_two_butt_pos:
                two_color = pygame.Color('lightskyblue4')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    twoplayer.startGame(1, "Easy", name)
                    # twoplayer.twoPlayer(1, "Easy", "Melvs")
            else:
                two_color = pygame.Color('lightskyblue3')
            pygame.display.update()
    else:
        pickgames.pick_games(name)
        pygame.display.update()


    pygame.init()
    pygame.display.update()
# pickMode()
