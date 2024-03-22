import pygame
import random
import sys
# import insertname
import pickgames.snakes.set_snake_highscore as get_highscore
import pickgames.pickgames as pickgames

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)


def gameLoop(name):
    user_name = name

    dis_width = 480
    dis_height = 480
    dis = pygame.display.set_mode((dis_width, dis_height))

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_block = 10
    snake_speed = 15

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(60, dis_height - snake_block) / 10.0) * 10.0

    clock = pygame.time.Clock()

    font_style = pygame.font.SysFont("bahnschrift", 20)
    score_font = pygame.font.SysFont("comicsansms", 15)
    position = ""
    # end = 10

    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, black)
        dis.blit(value, [0, 0])

    def High_Score(score):
        value = get_highscore.display_HighScore()
        if value is not None:
            if score > value[1]:
                dis_name = name
                dis_score = score
            else:
                dis_name = value[0]
                dis_score = value[1]
            display = score_font.render("High Score: " + dis_name + " " + str(dis_score), True, black)
        else:
            display = score_font.render("No High Score", True, black)
        dis.blit(display, [0, 20])

    def Save_Score(score):
        get_highscore.save_high_score(score, user_name)

    def our_snake(snake_list):
        for snake_x in snake_list:
            pygame.draw.rect(dis, red, [snake_x[0], snake_x[1], snake_block, snake_block])

    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 9, dis_height / 3])

    while not game_over:
        High_Score(Length_of_snake - 1)
        if game_close:
            Save_Score(Length_of_snake - 1)
        while game_close:
            pygame.draw.rect(dis, yellow, [0, 40, dis_width, dis_height])
            message("You Lost! Press C to Play Again or Q-Quit", black)
            # Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                    elif event.key == pygame.K_ESCAPE:
                        game_close = False
                        game_over = True
                    elif event.key == pygame.K_c:
                        gameLoop(name)
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and position != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    position = "left"
                elif event.key == pygame.K_RIGHT and position != "left":
                    x1_change = snake_block
                    y1_change = 0
                    position = "right"
                elif event.key == pygame.K_UP and position != "down":
                    y1_change = -snake_block
                    x1_change = 0
                    position = "up"
                elif event.key == pygame.K_DOWN and position != "up":
                    y1_change = snake_block
                    x1_change = 0
                    position = "down"
                elif event.key == pygame.K_ESCAPE:
                    game_close = False
                    game_over = True

        pygame.display.update()
        # if x1 >= dis_width or y1 >= dis_height or x1 < 0 or y1 < 25:
        #     game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        # if x1 == food_x and y1 == food_y:
            # end = 10
            # game_close = False
        if x1 >= dis_width:
            x1 = 0
        elif x1 < 0:
            x1 = dis_width
        elif y1 >= dis_height:
            y1 = 40
        elif y1 < 40:
            y1 = dis_height
        pygame.draw.rect(dis, yellow, [0, 40, dis_width, dis_height])
        pygame.draw.rect(dis, red, [food_x, food_y, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_List)
        head = font_style.render(user_name, True, '#000000')
        dis.blit(head, (x1, y1 - 20))
        Your_score(Length_of_snake - 1)

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(60, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    else:
        pickgames.pick_games(name)
        pygame.display.set_mode([360, 720])
    pygame.display.update()
