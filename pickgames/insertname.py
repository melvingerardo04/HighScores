import pygame
import sys
import pickgames.pickgames as pickgames
from pygame import  mixer



def insert_name():
    display = pygame.display.set_mode([360, 720])
    base_font = pygame.font.SysFont("Calibri", 35, True, False)
    user_text = ''
    input_rect = pygame.Rect(80, 360, 220, 50)
    enter_rect = pygame.Rect(80, 420, 220, 50)
    input_color = pygame.Color('lightskyblue3')
    enter_color = pygame.Color('lightskyblue3')

    width = display.get_width()
    height = display.get_height()
    run = True

    while run:
        mouse_cursor = pygame.mouse.get_pos()
        display.fill((255, 255, 255))
        pygame.draw.rect(display, input_color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        display.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(220, text_surface.get_width() + 10)

        pygame.draw.rect(display, enter_color, enter_rect)
        enter_text = base_font.render("Enter", True, (255, 255, 255))
        display.blit(enter_text, (enter_rect.x + 70, enter_rect.y + 10))
        for eve in pygame.event.get():
            if eve.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eve.type == pygame.KEYDOWN:
                if eve.key == pygame.K_ESCAPE:
                    run = False
                elif eve.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                elif user_text == '' and eve.key == pygame.K_RETURN :
                    font = pygame.font.SysFont("Calibri", 20, True, False)
                    enter_text = font.render("Please Input Name First", True, (255, 0, 0))
                    display.blit(enter_text, (input_rect.x + 10, input_rect.y + 15))
                elif eve.key != pygame.K_RETURN:
                    user_text += eve.unicode
                elif eve.key == pygame.K_RETURN:
                    if user_text != '':
                        pickgames.pick_games(user_text)
                    else:
                        font = pygame.font.SysFont("Calibri", 20, True, False)
                        enter_text = font.render("Please Input Name First", True, (255, 0, 0))
                        display.blit(enter_text, (input_rect.x + 10, input_rect.y + 15))

            if width - 280 <= mouse_cursor[0] <= width - 60 and height - 300 <= mouse_cursor[1] <= height - 250:
                enter_color = pygame.Color('lightskyblue4')
                if eve.type == pygame.MOUSEBUTTONDOWN:
                    mixer.music.load('Sounds/click.mp3')
                    mixer.music.play()

                    if user_text != '':
                        pickgames.pick_games(user_text)
                    else:
                        font = pygame.font.SysFont("Calibri", 20, True, False)
                        enter_text = font.render("Please Input Name First", True, (255, 0, 0))
                        display.blit(enter_text, (input_rect.x + 10, input_rect.y + 15))
            else:
                enter_color = pygame.Color('lightskyblue3')

            pygame.display.update()
    else:
        pickgames.pick_games(user_text)


pygame.display.update()

