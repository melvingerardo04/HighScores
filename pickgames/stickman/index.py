import sys
import pygame
import random

dis_width = 720
dis_height = 480
screen = pygame.display.set_mode((dis_width, dis_height))
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
fps = 24


class Enemy:
    enemy_x = 0
    enemy_y = 0
    enemy_image_size = 0
    enemy_image_range = (0, 0)
    enemy_image_url = ""
    enemy_image_loop = True
    image_Flip = True

    def __init__(self, x, y, enemy_image_size, enemy_image_range, enemy_image_url, enemy_image_loop, image_Flip):
        self.enemy_name_image = 0
        self.enemy_x = x
        self.enemy_y = y
        self.enemy_image_size = enemy_image_size
        self.enemy_image_range = enemy_image_range
        self.enemy_image_url = enemy_image_url
        self.enemy_image_loop = enemy_image_loop
        self.image_Flip = image_Flip

    def image(self):
        self.enemy_name_image += 1
        enemy_image = pygame.image.load("images/" + self.enemy_image_url + str(self.enemy_name_image) + ".png").convert_alpha()
        enemy_image = pygame.transform.scale(enemy_image, self.enemy_image_size)
        if self.image_Flip:
            enemy_image = pygame.transform.flip(enemy_image, True, False)
        screen.blit(enemy_image, (self.enemy_x, self.enemy_y))
        if self.enemy_name_image == self.enemy_image_range:
            self.enemy_name_image = 0


class StickMan:
    stick_man_x = 0
    stick_man_y = 0
    image_size = (0, 0)
    image_range = 0
    image_url = ""
    image_loop = True
    enemy = None
    image_Flip = True
    enemy_image_id = 0

    def __init__(self, x, y, image_size, image_range, image_url, image_loop):
        self.name_image = 0
        self.stick_man_x = x
        self.stick_man_y = y
        self.image_size = image_size
        self.image_range = image_range
        self.image_url = image_url
        self.image_loop = image_loop

    def image(self):
        self.name_image += 1
        stick_man = pygame.image.load("images/" + self.image_url + str(self.name_image) + ".png").convert_alpha()
        stick_man = pygame.transform.scale(stick_man, self.image_size)
        screen.blit(stick_man, (self.stick_man_x, self.stick_man_y))

        if self.image_loop:
            if self.name_image == self.image_range:
                self.name_image = 0
        else:
            if self.name_image == self.image_range:
                self.name_image = 0
                self.__init__(self.stick_man_x, 360, (120, 120), 8, "running_stickman/", True)

    def enemy_image(self):
        self.enemy_image_id = random.randint(1, 3)
        if self.enemy_image_id == 1:
            self.enemy = Enemy(720, 240, (250, 250), 23, "enemy_car/", True, False)
        elif self.enemy_image_id == 2:
            self.enemy = Enemy(720, 280, (250, 250), 16, "enemy_bird/", True, False)
        else:
            self.enemy = Enemy(720, 360, (120, 120), 16, "running_stickman/", True, True)


def start():
    screen = pygame.display.set_mode((dis_width, dis_height))
    run = True
    character = StickMan(0, 360, (120, 120), 8, "running_stickman/", True)
    character.enemy_image()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                if event.key == pygame.K_d:
                    character.stick_man_x += 10
                if event.key == pygame.K_a:
                    character.stick_man_x -= 10
                if event.key == pygame.K_q:
                    character.__init__(character.stick_man_x, 360, (120, 120), 17, "punch_stickman/", False)
                    if character.enemy.enemy_x <= 20:
                        character.enemy_image()

                if event.key == pygame.K_c:
                    character.__init__(character.stick_man_x, 360, (120, 120), 25, "crouch_stickman/", False)

                if event.key == pygame.K_e:
                    character.__init__(character.stick_man_x, 360, (120, 120), 26, "shoot/", False)
                if event.key == pygame.K_SPACE:
                    if character.stick_man_y >= 360:
                        character.stick_man_y -= 150
        screen.fill(white)
        character.image()
        character.enemy.image()
        if 720 >= character.enemy.enemy_x:
            character.enemy.enemy_x -= 10
        if character.enemy.enemy_x < -100:
            character.enemy_image()

        if character.stick_man_y <= 360:
            character.stick_man_y += 5

        clock.tick(fps)
        pygame.display.update()
    else:
        pygame.display.set_mode([360, 720])


# start()
