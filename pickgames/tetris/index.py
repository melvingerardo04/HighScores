import sys

import pygame
import random
import pickgames.tetris.set_tetris_highscore as sethighscore
from pygame import mixer
# from pickgames.tetris import difficulties as diff
from pickgames.tetris import mode

mixer.init()

# Shapes of the blocks
shapes = [
    [[]],
    [[4, 5, 6, 7], [1, 5, 9, 13]],  # straight
    [[4, 5, 9, 10], [2, 6, 5, 9]],  # z shape
    [[6, 7, 9, 10], [1, 5, 6, 10]],  # s shape green
    [[0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10], [2, 1, 5, 9]],  # J shape blue
    [[3, 5, 6, 7], [1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11]],  # L Shape yellow
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # i shape
    [[1, 2, 5, 6]],  # box
]
# Colors of the blocks

shapeColors = [(0, 255, 255), (0, 255, 255),  # straight light blue
               (255, 0, 0),  # z shape red
               (0, 255, 0),  # s shape green
               (0, 0, 255),  # J shape blue
               (255, 127, 0),  # L shape light orrage
               (128, 0, 128),  # i shape purple
               (255, 255, 0)]  # box shape yello
width = 500
height = 1000
gameWidth = 100  # meaning 300 // 10 = 30 width per block
gameHeight = 400  # meaning 600 // 20 = 20 height per blo ck
blockSize = 20

topLeft_x = (width - gameWidth) // 2
topLeft_y = height - gameHeight - 50


class Block:
    x = 0
    y = 0
    n = 0
    ghost_y = 19

    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.type = n
        self.color = n
        self.rotation = 0

    def image(self):
        return shapes [self.type] [self.rotation]

    def rotate(self):
        self.rotation = (self.rotation - 1) % len(shapes [self.type])


class Tetris:
    level = 0
    score = 0
    gameHighScore = 0
    state = "start"
    field = []
    height = 0
    e = 0
    zoom = 20
    x = 100
    y = 60
    block = None
    nextBlock = None
    holdBlock = None

    # Sets the properties of the board
    def __init__(self, height, width, field):
        self.height = height
        self.width = width
        self.field = field
        for i in range(height):
            new_line = []
            for j in range(width):
                new_line.append(0)
            self.field.append(new_line)

    # Creates a new block
    def new_block(self):
        self.block = Block(3, 0, random.randint(1, len(shapes) - 2))

    def next_block(self):
        self.nextBlock = Block(3, 0, random.randint(1, len(shapes) - 1))

    def hold_block(self):
        self.holdBlock = self.block

    # Checks if the blocks touch the top of the board
    def intersects(self):
        intersection = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or \
                            j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or \
                            self.field [i + self.block.y] [j + self.block.x] > 0:
                        intersection = True
        return intersection

    # Checks if a row is formed and destroys that line
    def break_lines(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field [i] [j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i1 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field [i1] [j] = self.field [i1 - 1] [j]
        self.level += .01
        self.score += lines ** 1
        #  This function runs once the block reaches the bottom.

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.field [i + self.block.y] [j + self.block.x] = self.block.color
        self.break_lines()  # Checking if any row is formed
        self.block = self.nextBlock
        self.next_block()  # Creating a new block
        if self.intersects():  # If blocks touch the top of the board, then ending the game by setting status as gameover
            self.state = "gameover"

    # display the next  block
    def draw_next_block(self):
        sx = topLeft_x + gameWidth + 20
        sy = topLeft_y + gameHeight / 2 - 680
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in self.nextBlock.image():
                    pygame.draw.rect(screen, shapeColors [self.nextBlock.color], (sx + j * 20, sy + i * 20, 20, 20), 0)

    # display the hold block
    def draw_hold_block(self):
        if self.holdBlock is not None:
            sx = topLeft_x + gameWidth - 300
            sy = topLeft_y + gameHeight / 2 - 680
            self.holdBlock.y = 1
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in self.holdBlock.image():
                        pygame.draw.rect(screen, shapeColors [self.holdBlock.color], (sx + j * 20, sy + i * 20, 20, 20),
                                         0)

    # Moves the block to the bottom
    def moveBottom(self):
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

    # Moves the block down by a unit
    def moveDown(self):
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    # This function moves the block horizontally
    def moveHoriz(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

        while self.block.ghost_y != 18:
            self.block.ghost_y += 1
        self.draw_ghost_block()

    # This function rotates the block
    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation
        self.draw_ghost_block()
        while self.block.ghost_y != 18:
            self.block.ghost_y += 1

    # display the ghost block
    def draw_ghost_block(self):
        if self.block is not None and self.state != "gameover":
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in self.block.image():
                        if i + self.block.ghost_y <= self.height - 1 and self.block.ghost_y >= 0 or j + self.block.x > self.width - 1:
                            if self.field [i + self.block.ghost_y] [j + self.block.x] or \
                                    self.field [i + self.block.ghost_y - 1] [j + self.block.x]:
                                self.block.ghost_y -= 1

                        else:
                            self.block.ghost_y -= 1
                        pygame.draw.rect(screen, shapeColors [self.block.color],
                                         [self.x + self.zoom * (j + self.block.x) + 1,
                                          self.y + self.zoom * (i + self.block.ghost_y),
                                          self.zoom - 2, self.zoom - 1], 1)

def displayText(message, x, y, fontSize):
    font = pygame.font.SysFont('Calibri', fontSize, True, False)
    display = font.render(message, True, '#000000')
    return screen.blit(display, [x, y])


def startGame(level, difficulties, name):
    game_over = False
    game_close = False
    clock = pygame.time.Clock()
    fps = 30
    game = Tetris(20, 10, [])
    counter = 0
    game.level = level
    pressing_down = False
    font = pygame.font.SysFont('Calibri', 20, True, False)

    while not game_over:
        # Create a new block if there is no moving block
        screen = pygame.display.set_mode([720, 720])
        if game.block is None:
            game.new_block()
        if game.nextBlock is None:
            game.next_block()
        counter += 1  # Keeping track if the time
        if counter > 100000:
            counter = 0

        # Moving the block continuously with time or when down key is pressed
        if counter % (fps // game.level // 2) == 0 or pressing_down:
            if game.state == "start":
                game.moveDown()
        # Checking which key is pressed and running corresponding function
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.rotate()
                if event.key == pygame.K_DOWN:
                    game.moveDown()
                if event.key == pygame.K_LEFT:
                    game.moveHoriz(-1)
                if event.key == pygame.K_RIGHT:
                    game.moveHoriz(1)
                if event.key == pygame.K_SPACE:
                    game.moveBottom()
                if event.key == pygame.K_LSHIFT or event.key == pygame.K_c:
                    if game.holdBlock is None:
                        game.holdBlock = game.block
                        game.block = game.nextBlock
                        game.next_block()
                    else:
                        switch_block = game.holdBlock
                        game.holdBlock = game.block
                        game.block = switch_block
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    if game.state == "gameover":
                        game_over = True
                if event.key == pygame.K_RETURN:
                    if game.state == "gameover":
                        startGame(level, difficulties, name)
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                    mixer.music.pause()
                    pygame.display.update()
        # Update the color of the board base on difficulties
        if difficulties == "Easy":
            screen.fill("#808080")
            get_high_score = sethighscore.displayEasyHighScore(game.score)
        elif difficulties == "Medium":
            screen.fill("#FFA6C9")
            get_high_score = sethighscore.displayMediumHighScore(game.score)
        else:
            screen.fill("#bcbccc")
            get_high_score = sethighscore.displayHardHighScore(game.score)
        # display high score
        if get_high_score is None:
            if game.score >= 1:
                displayText("High Score: You " + str(game.score), 310, 20, 20)
            else:
                displayText("No High Score", 310, 20, 20)
        elif game.score >= get_high_score[0]:
            displayText("High Score: You " + str(game.score), 310, 20, 20)
        else:
            displayText("High Score: " + get_high_score [1] + " " + str(get_high_score [0]), 310, 20, 20)

        # Updating the game board regularly
        for i in range(game.height):
            for j in range(game.width):
                pygame.draw.rect(screen, '#FFFFFF',
                                 [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
                if game.field[i][j] > 0:
                    pygame.draw.rect(screen, shapeColors[game.field[i][j]],
                                     [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2,
                                      game.zoom - 1])

        # Updating the board with the moving block
        if game.block is not None:
            for i in range(4):
                for j in range(4):
                    p = i * 4 + j
                    if p in game.block.image():
                        pygame.draw.rect(screen, shapeColors[game.block.color],
                                         [game.x + game.zoom * (j + game.block.x) + 1,
                                          game.y + game.zoom * (i + game.block.y) + 1,
                                          game.zoom - 2, game.zoom - 2])

        # Showing the score
        displayText("Score: " + str(game.score), 310, 0, 20)
        displayText("Next Shape ", 310, 50, 20)
        displayText("Hold ", 30, 50, 20)

        # Ending the game if state is Game Over
        game.draw_ghost_block()
        game.draw_hold_block()
        game.draw_next_block()
        if game.state == "gameover":
            if difficulties == "Easy":
                screen.fill("#808080")
            elif difficulties == "Medium":
                screen.fill("#FFA6C9")
            else:
                screen.fill("#bcbccc")
            save_score = sethighscore.saveHighScore(name, game.score, get_high_score, difficulties)
            save = save_score
            saveFont = pygame.font.SysFont('Calibri', 50, True, False)
            saveText = saveFont.render(save, True, '#000000')
            screen.blit(saveText, [30, 300])
            displayText("Press ESC / Q to Quit or Enter to Play Again", 60, 360, 20)
            while game_close:
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
                        elif event.key == pygame.K_RETURN:
                            startGame(level, difficulties, name)
                pygame.display.update()
        game_close = True
        pygame.display.update()
        clock.tick(fps)

    else:
        mode.pickMode(name)
        pygame.display.set_mode([720, 720])


pygame.font.init()
screen = pygame.display.set_mode([1020, 720])
pygame.display.update()
