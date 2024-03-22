import pygame
import sys
import pickgames.pickgames as pickgames


WIDTH = 600
ROWS = 8

WIN = pygame.display.set_mode((WIDTH, WIDTH))
RED = pygame.image.load('images/checkers/red.png')
Dark = pygame.image.load('images/checkers/dark.png')

REDKING = pygame.image.load('images/checkers/redking.png')
DarkKING = pygame.image.load('images/checkers/darkking.png')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (235, 168, 52)
BLUE = (76, 252, 241)

pygame.init()
priorMoves = []


class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.piece = None

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / ROWS, WIDTH / ROWS))
        if self.piece:
            WIN.blit(self.piece.image, (self.x + 14, self.y + 14))


def update_display(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()


def make_grid(rows, width):
    grid = []
    gap = width // rows
    count = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j, i, gap)
            if abs(i - j) % 2 == 0:
                node.colour = BLACK
            if (abs(i + j) % 2 == 0) and (i < 3):
                node.piece = Piece('R')
            elif (abs(i + j) % 2 == 0) and i > 4:
                node.piece = Piece('D')
            count += 1
            grid [i].append(node)
    return grid


def draw_grid(win, rows, width):
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))


class Piece:
    def __init__(self, team):
        self.team = team
        self.image = RED if self.team == 'R' else Dark
        self.type = None

    def draw(self, x, y):
        WIN.blit(self.image, (x, y))


def getNode(grid, rows, width):
    gap = width // rows
    RowX, RowY = pygame.mouse.get_pos()
    Row = RowX // gap
    Col = RowY // gap

    return Col, Row


def resetColours(grid, node):
    positions = generatePotentialMoves(node, grid)
    positions.append(node)

    for colouredNodes in positions:
        nodeX, nodeY = colouredNodes
        grid [nodeX] [nodeY].colour = BLACK if abs(nodeX - nodeY) % 2 == 0 else WHITE


def HighlightpotentialMoves(piecePosition, grid):
    positions = generatePotentialMoves(piecePosition, grid)
    for position in positions:
        Column, Row = position
        grid[Column][Row].colour = BLUE


def opposite(team):
    return "R" if team == "D" else "D"


def generatePotentialMoves(nodePosition, grid):
    checker = lambda x, y: x + y >= 0 and x + y < 8
    positions = []
    column, row = nodePosition
    if grid[column][row].piece:
        vectors = [[1, -1], [1, 1]] if grid[column][row].piece.team == "R" else [[-1, -1], [-1, 1]]
        if grid[column][row].piece.type == 'KING':
            vectors = [[1, -1], [1, 1], [-1, -1], [-1, 1]]
        for vector in vectors:
            columnVector, rowVector = vector
            if checker(columnVector, column) and checker(rowVector, row):
                if not grid[(column + columnVector)][(row + rowVector)].piece:
                    positions.append((column + columnVector, row + rowVector))
                    # checking ng movement kung may pwede pang kainin
                elif grid[(column + columnVector)][(row + rowVector)].piece and \
                        grid[column + columnVector][row + rowVector].piece.team == opposite(grid[column][row].piece.team):
                    # checking kung pwede kainin
                    if checker((2 * columnVector), column) and checker((2 * rowVector), row) \
                            and not grid[(2 * columnVector) + column][(2 * rowVector) + row].piece:
                        positions.append((2 * columnVector + column, 2 * rowVector + row))
    return positions


def highlight(ClickedNode, Grid, OldHighlight):
    Column, Row = ClickedNode
    Grid[Column][Row].colour = ORANGE
    if OldHighlight:
        resetColours(Grid, OldHighlight)
    HighlightpotentialMoves(ClickedNode, Grid)
    return Column, Row


def move(grid, piecePosition, newPosition):
    resetColours(grid, piecePosition)
    newColumn, newRow = newPosition
    oldColumn, oldRow = piecePosition
    piece = grid[oldColumn][oldRow].piece
    grid[newColumn][newRow].piece = piece
    grid[oldColumn][oldRow].piece = None

    if newColumn == 7 and grid[newColumn][newRow].piece.team == 'R':
        grid[newColumn][newRow].piece.type = 'KING'
        grid[newColumn][newRow].piece.image = REDKING
    if newColumn == 0 and grid[newColumn][newRow].piece.team == 'D':
        grid[newColumn][newRow].piece.type = 'KING'
        grid[newColumn][newRow].piece.image = DarkKING
    if abs(newColumn - oldColumn) == 2 or abs(newRow - oldRow) == 2:  # condition for eating pieces
        grid[int((newColumn + oldColumn) / 2)][int((newRow + oldRow) / 2)].piece = None  # remove piece after eating the pieces
        # print(newColumn, newRow)
        if not generatePotentialMoves((newColumn, newRow), grid):
            return opposite(grid[newColumn][newRow].piece.team)
        nextMoves = generatePotentialMoves((newColumn, newRow), grid)
        nextMoveColumns = []
        nextMoveRows = []
        next = []
        for nextMove in range(len(nextMoves)):
            nextMoveColumns.append(nextMoves[nextMove][0])
            nextMoveRows.append(nextMoves[nextMove][1])
        for nextMoveColumn in nextMoveColumns:
            if abs(nextMoveColumn - newColumn) == 1:
                next.append(1)
            elif abs(nextMoveColumn - newColumn) == 2:
                next.append(2)
        for nextMoveRow in nextMoveRows:
            if abs(nextMoveRow - newRow) == 1:
                next.append(1)
            elif abs(nextMoveRow - newRow) == 2:
                next.append(2)
        for move in next:
            if move == 2:
                return grid[newColumn][newRow].piece.team
    return opposite(grid[newColumn][newRow].piece.team)


def main(name):
    grid = make_grid(ROWS, WIDTH)
    highlightedPiece = None
    currMove = 'D'
    WIN = pygame.display.set_mode((WIDTH, WIDTH))
    pygame.display.set_caption('Checkers')
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pickgames.pick_games(name)
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickedNode = getNode(grid, ROWS, WIDTH)
                ClickedPositionColumn, ClickedPositionRow = clickedNode
                if grid[ClickedPositionColumn][ClickedPositionRow].colour == BLUE:
                    if highlightedPiece:
                        pieceColumn, pieceRow = highlightedPiece
                    if currMove == grid[pieceColumn][pieceRow].piece.team:
                        resetColours(grid, highlightedPiece)
                        currMove = move(grid, highlightedPiece, clickedNode)
                elif highlightedPiece == clickedNode:
                    pass
                else:
                    if grid[ClickedPositionColumn][ClickedPositionRow].piece:
                        if currMove == grid[ClickedPositionColumn][ClickedPositionRow].piece.team:
                            highlightedPiece = highlight(clickedNode, grid, highlightedPiece)
        update_display(WIN, grid, ROWS, WIDTH)

# main(WIDTH, ROWS)
