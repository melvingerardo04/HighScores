import pygame
import sys
import pickgames.pickgames as pick
from pickgames import insertname
from pygame import mixer
from games import menu

def menu():
    # screen resolution
    res = (360, 720)
    screen = pygame.display.set_mode(res)

    pygame.display.set_caption("Created By Melvs")
    font = pygame.font.SysFont("Calibri", 40, True, False)

    # defining a font
    labelStart = font.render("Start", True, '#FFFFFF')
    labelQuit = font.render("Quit", True, '#FFFFFF')

    start_rect = pygame.Rect(90, 380, 200, 50)
    start_color = pygame.Color('lightskyblue3')

    quit_rect = pygame.Rect(90, 440, 200, 50)
    quit_color = pygame.Color('lightskyblue3')

    run = True
    fps = 120
    clock = pygame.time.Clock()
    imp_x = 0

    def boat(boat_x, boat_y):
        boat_image = pygame.image.load("images/boat.png").convert_alpha()
        DEFAULT_IMAGE_SIZE = (100, 100)
        boat_image = pygame.transform.scale(boat_image, DEFAULT_IMAGE_SIZE)
        screen.blit(boat_image, (boat_x, boat_y))

    def sunset(sunset_x, sunset_y):
        sunset_image = pygame.image.load("images/sunset.jpg").convert_alpha()
        DEFAULT_IMAGE_SIZE = (360, 720)
        sunset_image = pygame.transform.scale(sunset_image, DEFAULT_IMAGE_SIZE)
        screen.blit(sunset_image, (sunset_x, sunset_y))

    while run:
        imp_x += 0.5
        if imp_x == 360:
            imp_x = 0
        sunset(0, 0)
        boat(imp_x, 280)
        mouse = pygame.mouse.get_pos()
        get_start_butt_pos = start_rect.x <= mouse[0] <= start_rect.x + 200 and start_rect.y <= mouse[1] <= start_rect.y + 50
        get_quit_butt_pos = quit_rect.x <= mouse[0] <= quit_rect.x + 200 and quit_rect.y <= mouse[1] <= quit_rect.y + 50

        pygame.draw.rect(screen, start_color, start_rect)
        pygame.draw.rect(screen, quit_color, quit_rect)

        screen.blit(labelStart, (start_rect.x + 55, start_rect.y + 5))
        screen.blit(labelQuit, (quit_rect.x + 60, quit_rect.y + 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            # hover for start button
            if get_start_butt_pos:
                start_color = pygame.Color('lightskyblue4')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()
                    # pick.pick_games()
                    insertname.insert_name()
            else:
                start_color = pygame.Color('lightskyblue3')

            # hover for quit button
            if get_quit_butt_pos:
                quit_color = pygame.Color('lightskyblue4')
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.quit()
                    sys.exit()
            else:
                quit_color = pygame.Color('lightskyblue3')

        clock.tick(fps)
        pygame.display.update()


menu()
