import random
import threading

import pygame
import pymsgbox
from pygame.locals import *
from pymsgbox import *

FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 1200  # size of window's width in pixels
WINDOWHEIGHT = 800  # size of windows' height in pixels
REVEALSPEED = 8  # speed boxes' sliding reveals and covers
BOXSIZE = 225  # size of box height & width in pixels
GAPSIZE = 10  # size of gap between boxes in pixels
BOARDWIDTH = 4  # number of columns of icons
BOARDHEIGHT = 3  # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = (60,   60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (0,   255,   0)
BLUE     = (0,     0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (0,   255, 255)

# activate the pygame library .
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# define the RGB value
# for white colour
white = (255, 255, 255)

# assigning values to X and Y variable
X = 225
Y = 225

# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

# set the pygame window name
pygame.display.set_caption('Image')

# create a surface object, image is drawn on it.
image_1 = pygame.image.load(r'D:\Image\CW Python\fox.png')
# create a surface object, image is drawn on it.
image_2 = pygame.image.load(r'D:\Image\CW Python\maco.png')
# create a surface object, image is drawn on it.
image_3 = pygame.image.load(r'D:\Image\CW Python\gold_fish.png')
# create a surface object, image is drawn on it.
image_4 = pygame.image.load(r'D:\Image\CW Python\avenger.png')
# create a surface object, image is drawn on it.
image_5 = pygame.image.load(r'D:\Image\CW Python\ball.png')
# create a surface object, image is drawn on it.
image_6 = pygame.image.load(r'D:\Image\CW Python\boy.png')
# create a surface object, image is drawn on it.
image_7 = pygame.image.load(r'D:\Image\CW Python\cat.png')
# create a surface object, image is drawn on it.
image_8 = pygame.image.load(r'D:\Image\CW Python\earth.png')
# create a surface object, image is drawn on it.
image_9 = pygame.image.load(r'D:\Image\CW Python\fire.png')
# create a surface object, image is drawn on it.
image_10 = pygame.image.load(r'D:\Image\CW Python\google.png')
# create a surface object, image is drawn on it.
image_11 = pygame.image.load(r'D:\Image\CW Python\halloween.png')
# create a surface object, image is drawn on it.
image_12 = pygame.image.load(r'D:\Image\CW Python\ice_cream.png')
# create a surface object, image is drawn on it.
image_13 = pygame.image.load(r'D:\Image\CW Python\lion.png')
# create a surface object, image is drawn on it.
image_14 = pygame.image.load(r'D:\Image\CW Python\love.png')
# create a surface object, image is drawn on it.
image_15 = pygame.image.load(r'D:\Image\CW Python\men.png')
# create a surface object, image is drawn on it.
image_16 = pygame.image.load(r'D:\Image\CW Python\phone.png')
# create a surface object, image is drawn on it.
image_17 = pygame.image.load(r'D:\Image\CW Python\pizza.png')
# create a surface object, image is drawn on it.
image_18 = pygame.image.load(r'D:\Image\CW Python\razer.png')
# create a surface object, image is drawn on it.
image_19 = pygame.image.load(r'D:\Image\CW Python\snap.png')
# create a surface object, image is drawn on it.
image_20 = pygame.image.load(r'D:\Image\CW Python\water.png')
# create a surface object, image is drawn on it.
image_21 = pygame.image.load(r'D:\Image\CW Python\beer.png')
# create a surface object, image is drawn on it.
image_22 = pygame.image.load(r'D:\Image\CW Python\meter.png')
# create a surface object, image is drawn on it.
image_23 = pygame.image.load(r'D:\Image\CW Python\camera.png')
# create a surface object, image is drawn on it.
image_24 = pygame.image.load(r'D:\Image\CW Python\adidas.png')
# create a surface object, image is drawn on it.
image_25 = pygame.image.load(r'D:\Image\CW Python\barcode.png')
# create a surface object, image is drawn on it.
image_26 = pygame.image.load(r'D:\Image\CW Python\chelsea.png')
# create a surface object, image is drawn on it.
image_27 = pygame.image.load(r'D:\Image\CW Python\coca_cola.png')
# create a surface object, image is drawn on it.
image_28 = pygame.image.load(r'D:\Image\CW Python\controller.png')
# create a surface object, image is drawn on it.
image_29 = pygame.image.load(r'D:\Image\CW Python\dinosaur.png')
# create a surface object, image is drawn on it.
image_30 = pygame.image.load(r'D:\Image\CW Python\europe.png')
# create a surface object, image is drawn on it.
image_31 = pygame.image.load(r'D:\Image\CW Python\fc_bayern.png')
# create a surface object, image is drawn on it.
image_32 = pygame.image.load(r'D:\Image\CW Python\juventes.png')
# create a surface object, image is drawn on it.
image_33 = pygame.image.load(r'D:\Image\CW Python\laptop.png')
# create a surface object, image is drawn on it.
image_34 = pygame.image.load(r'D:\Image\CW Python\levis.png')
# create a surface object, image is drawn on it.
image_35 = pygame.image.load(r'D:\Image\CW Python\link.png')
# create a surface object, image is drawn on it.
image_36 = pygame.image.load(r'D:\Image\CW Python\mcdonalds.png')
# create a surface object, image is drawn on it.
image_37 = pygame.image.load(r'D:\Image\CW Python\olympic.png')
# create a surface object, image is drawn on it.
image_38 = pygame.image.load(r'D:\Image\CW Python\overwatch.png')
# create a surface object, image is drawn on it.
image_40 = pygame.image.load(r'D:\Image\CW Python\r6.png')
# create a surface object, image is drawn on it.
image_41 = pygame.image.load(r'D:\Image\CW Python\r6_doc.png')
# create a surface object, image is drawn on it.
image_43 = pygame.image.load(r'D:\Image\CW Python\society.png')
# create a surface object, image is drawn on it.
image_44 = pygame.image.load(r'D:\Image\CW Python\spotify.png')
# create a surface object, image is drawn on it.
image_45 = pygame.image.load(r'D:\Image\CW Python\tree.png')
# create a surface object, image is drawn on it.
image_46 = pygame.image.load(r'D:\Image\CW Python\turn_on.png')
# create a surface object, image is drawn on it.
image_47 = pygame.image.load(r'D:\Image\CW Python\twitch.png')
# create a surface object, image is drawn on it.
image_48 = pygame.image.load(r'D:\Image\CW Python\twitter.png')
# create a surface object, image is drawn on it.
image_49 = pygame.image.load(r'D:\Image\CW Python\ubisoft.png')
# create a surface object, image is drawn on it.
image_50 = pygame.image.load(r'D:\Image\CW Python\unity.png')
# create a surface object, image is drawn on it.
image_51 = pygame.image.load(r'D:\Image\CW Python\usa.png')
# create a surface object, image is drawn on it.
image_52 = pygame.image.load(r'D:\Image\CW Python\whatsapp.png')
# create a surface object, image is drawn on it.
image_53 = pygame.image.load(r'D:\Image\CW Python\wildlands.png')
# create a surface object, image is drawn on it.
image_54 = pygame.image.load(r'D:\Image\CW Python\wonder_woman.png')
# create a surface object, image is drawn on it.
image_55 = pygame.image.load(r'D:\Image\CW Python\youtube.png')


BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

IMAGE_19 = 'img_19'
IMAGE_20 = 'img_20'
IMAGE_21 = 'img_21'
IMAGE_22 = 'img_22'
IMAGE_23 = 'img_23'
IMAGE_1 = 'img_1'
IMAGE_2 = 'img_2'
IMAGE_3 = 'img_3'
IMAGE_4 = 'img_4'
IMAGE_5 = 'img_5'
IMAGE_6 = 'img_6'
IMAGE_7 = 'img_7'
IMAGE_8 = 'img_8'
IMAGE_9 = 'img_9'
IMAGE_10 = 'img_10'
IMAGE_11 = 'img_11'
IMAGE_12 = 'img_12'
IMAGE_13 = 'img_13'
IMAGE_14 = 'img_14'
IMAGE_15 = 'img_15'
IMAGE_16 = 'img_16'
IMAGE_17 = 'img_17'
IMAGE_18 = 'img_18'
IMAGE_24 = 'img_24'
IMAGE_25 = 'img_25'
IMAGE_26 = 'img_26'
IMAGE_27 = 'img_27'
IMAGE_28 = 'img_28'
IMAGE_29 = 'img_29'
IMAGE_30 = 'img_30'
IMAGE_31 = 'img_31'
IMAGE_32 = 'img_32'
IMAGE_33 = 'img_33'
IMAGE_34 = 'img_34'
IMAGE_35 = 'img_35'
IMAGE_36 = 'img_36'
IMAGE_37 = 'img_37'
IMAGE_38 = 'img_38'
IMAGE_40 = 'img_40'
IMAGE_41 = 'img_41'
IMAGE_43 = 'img_43'
IMAGE_44 = 'img_44'
IMAGE_45 = 'img_45'
IMAGE_46 = 'img_46'
IMAGE_47 = 'img_47'
IMAGE_48 = 'img_48'
IMAGE_49 = 'img_49'
IMAGE_50 = 'img_50'
IMAGE_51 = 'img_51'
IMAGE_52 = 'img_52'
IMAGE_53 = 'img_53'
IMAGE_54 = 'img_54'
IMAGE_55 = 'img_55'


Score = 0
Time = 0
timer = 60
output_time = ""
frame_count = 0
frame_rate = 61
runner = True
message = ""
pause = False
level = 1
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLICONS = (IMAGE_1, IMAGE_2, IMAGE_3, IMAGE_4, IMAGE_5,
            IMAGE_6, IMAGE_7, IMAGE_8, IMAGE_9, IMAGE_10,
            IMAGE_11, IMAGE_12, IMAGE_13, IMAGE_14, IMAGE_15,
            IMAGE_16, IMAGE_17, IMAGE_18, IMAGE_19, IMAGE_20,
            IMAGE_21, IMAGE_22, IMAGE_23, IMAGE_24, IMAGE_25,
            IMAGE_26, IMAGE_27, IMAGE_28, IMAGE_29, IMAGE_30,
            IMAGE_31, IMAGE_32, IMAGE_33, IMAGE_34, IMAGE_35,
            IMAGE_36, IMAGE_37, IMAGE_38, IMAGE_40,
            IMAGE_41, IMAGE_43, IMAGE_44, IMAGE_45,
            IMAGE_46, IMAGE_47, IMAGE_48, IMAGE_49, IMAGE_50,
            IMAGE_51, IMAGE_52, IMAGE_53, IMAGE_54, IMAGE_55,)
assert len(ALLCOLORS) * len(ALLICONS) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."

def main():
    global FPSCLOCK, DISPLAYSURF, runner, level, timer, message,Score
    pygame.init()

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))

    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Course Work')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)
    done = True
    timer_manager()
    while done:  # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(NAVYBLUE) # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                runner = False
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True
        boxx, boxy = getBoxAtPixel(mousex, mousey)
        if boxx != None and boxy != None:
            # The mouse is currently over a box.
            if not revealedBoxes[boxx][boxy]:
                drawHighlightBox(boxx, boxy)
            if not revealedBoxes[boxx][boxy] and mouseClicked:
                revealBoxesAnimation(mainBoard, [(boxx, boxy)])
                revealedBoxes[boxx][boxy] = True # set the box as "revealed"
                if firstSelection == None: # the current box was the first box clicked
                    firstSelection = (boxx, boxy)
                else: # the current box was the second box clicked
                    # Check if there is a match between the two icons.
                    icon1shape, icon1color = getShapeAndColor(mainBoard, firstSelection[0], firstSelection[1])
                    icon2shape, icon2color = getShapeAndColor(mainBoard, boxx, boxy)

                    if icon1shape != icon2shape or icon1color != icon2color:
                        # Icons don't match. Re-cover up both selections.
                        pygame.time.wait(1000) # 1000 milliseconds = 1 sec
                        coverBoxesAnimation(mainBoard, [(firstSelection[0], firstSelection[1]), (boxx, boxy)])
                        revealedBoxes[firstSelection[0]][firstSelection[1]] = False
                        revealedBoxes[boxx][boxy] = False
                        global Score
                        Score -= 5
                        # print("Score : " + str(Score))
                    elif hasWon(revealedBoxes): # check if all pairs found
                        level += 1
                        timer -= timer
                        timer += 64
                        message = ""

                        if(level < 3):
                            gameWonAnimation(mainBoard)
                            pygame.time.wait(2000)

                            # Reset the board
                            mainBoard = getRandomizedBoard()
                            revealedBoxes = generateRevealedBoxesData(False)

                            # Show the fully unrevealed board for a second.
                            drawBoard(mainBoard, revealedBoxes)
                            pygame.display.update()
                            pygame.time.wait(1000)

                            # Replay the start game animation.
                            startGameAnimation(mainBoard)
                        elif (level >= 3):
                            pymsgbox.alert('Your Score is : ' + str(Score), 'Score!')



                    firstSelection = None # reset firstSelection variable

        # Redraw the screen and wait a clock tick.
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def generateRevealedBoxesData(val):
    revealedBoxes = []
    for i in range(BOARDWIDTH):
        revealedBoxes.append([val] * BOARDHEIGHT)
    return revealedBoxes


def getRandomizedBoard():
    # Get a list of every possible shape in every possible color.
    icons = []
    for color in ALLCOLORS:
        for shape in ALLICONS:
            icons.append((shape, color))

    random.shuffle(icons) # randomize the order of the icons list
    numIconsUsed = int(BOARDWIDTH * BOARDHEIGHT / 4) # calculate how many icons are needed
    icons = icons[:numIconsUsed] * 4 # make four of each
    random.shuffle(icons)

    # Create the board data structure, with randomly placed icons.
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            column.append(icons[0])
            del icons[0] # remove the icons as we assign them
        board.append(column)
    return board


def splitIntoGroupsOf(groupSize, theList):
    # splits a list into a list of lists, where the inner lists have at
    # most groupSize number of items.
    result = []
    for i in range(0, len(theList), groupSize):
        result.append(theList[i:i + groupSize])
    return result


def leftTopCoordsOfBox(boxx, boxy):
    # Convert board coordinates to pixel coordinates
    left = boxx * (BOXSIZE + GAPSIZE) + XMARGIN
    top = boxy * (BOXSIZE + GAPSIZE) + YMARGIN
    return (left, top)


def getBoxAtPixel(x, y):
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            boxRect = pygame.Rect(left, top, BOXSIZE, BOXSIZE)
            if boxRect.collidepoint(x, y):
                return (boxx, boxy)
    return (None, None)


def drawIcon(shape, color, boxx, boxy):
    quarter = int(BOXSIZE * 0.25)  # syntactic sugar
    half = int(BOXSIZE * 0.5)  # syntactic sugar

    left, top = leftTopCoordsOfBox(boxx, boxy)  # get pixel coords from board coords
    # Draw the shapes
    if shape == IMAGE_1:
        display_surface.blit(image_1, (left, top))
    elif shape == IMAGE_2:
        display_surface.blit(image_2, (left, top))
    elif shape == IMAGE_3:
        display_surface.blit(image_3, (left, top))
    elif shape == IMAGE_4:
        display_surface.blit(image_4, (left, top))
    elif shape == IMAGE_5:
        display_surface.blit(image_5, (left, top))
    elif shape == IMAGE_6:
        display_surface.blit(image_6, (left, top))
    elif shape == IMAGE_7:
        display_surface.blit(image_7, (left, top))
    elif shape == IMAGE_8:
        display_surface.blit(image_8, (left, top))
    elif shape == IMAGE_9:
        display_surface.blit(image_9, (left, top))
    elif shape == IMAGE_10:
        display_surface.blit(image_10, (left, top))
    elif shape == IMAGE_11:
        display_surface.blit(image_11, (left, top))
    elif shape == IMAGE_12:
        display_surface.blit(image_12, (left, top))
    elif shape == IMAGE_13:
        display_surface.blit(image_13, (left, top))
    elif shape == IMAGE_14:
        display_surface.blit(image_14, (left, top))
    elif shape == IMAGE_15:
        display_surface.blit(image_15, (left, top))
    elif shape == IMAGE_16:
        display_surface.blit(image_16, (left, top))
    elif shape == IMAGE_17:
        display_surface.blit(image_17, (left, top))
    elif shape == IMAGE_18:
        display_surface.blit(image_18, (left, top))
    elif shape == IMAGE_19:
        display_surface.blit(image_19, (left, top))
    elif shape == IMAGE_20:
        display_surface.blit(image_20, (left, top))
    elif shape == IMAGE_21:
        display_surface.blit(image_21, (left, top))
    elif shape == IMAGE_22:
        display_surface.blit(image_22, (left, top))
    elif shape == IMAGE_23:
        display_surface.blit(image_23, (left, top))
    elif shape == IMAGE_24:
        display_surface.blit(image_24, (left, top))
    elif shape == IMAGE_25:
        display_surface.blit(image_25, (left, top))
    elif shape == IMAGE_26:
        display_surface.blit(image_26, (left, top))
    elif shape == IMAGE_27:
        display_surface.blit(image_27, (left, top))
    elif shape == IMAGE_28:
        display_surface.blit(image_28, (left, top))
    elif shape == IMAGE_29:
        display_surface.blit(image_29, (left, top))

    elif shape == IMAGE_30:
        display_surface.blit(image_30, (left, top))
    elif shape == IMAGE_31:
        display_surface.blit(image_31, (left, top))
    elif shape == IMAGE_32:
        display_surface.blit(image_32, (left, top))
    elif shape == IMAGE_33:
        display_surface.blit(image_33, (left, top))
    elif shape == IMAGE_34:
        display_surface.blit(image_34, (left, top))
    elif shape == IMAGE_35:
        display_surface.blit(image_35, (left, top))
    elif shape == IMAGE_36:
        display_surface.blit(image_36, (left, top))
    elif shape == IMAGE_37:
        display_surface.blit(image_37, (left, top))
    elif shape == IMAGE_38:
        display_surface.blit(image_38, (left, top))
    elif shape == IMAGE_40:
        display_surface.blit(image_40, (left, top))
    elif shape == IMAGE_41:
        display_surface.blit(image_41, (left, top))
    elif shape == IMAGE_43:
        display_surface.blit(image_43, (left, top))
    elif shape == IMAGE_44:
        display_surface.blit(image_44, (left, top))
    elif shape == IMAGE_45:
        display_surface.blit(image_45, (left, top))
    elif shape == IMAGE_46:
        display_surface.blit(image_46, (left, top))
    elif shape == IMAGE_47:
        display_surface.blit(image_47, (left, top))
    elif shape == IMAGE_48:
        display_surface.blit(image_48, (left, top))
    elif shape == IMAGE_49:
        display_surface.blit(image_49, (left, top))
    elif shape == IMAGE_50:
        display_surface.blit(image_50, (left, top))
    elif shape == IMAGE_51:
        display_surface.blit(image_51, (left, top))
    elif shape == IMAGE_52:
        display_surface.blit(image_52, (left, top))
    elif shape == IMAGE_53:
        display_surface.blit(image_53, (left, top))
    elif shape == IMAGE_54:
        display_surface.blit(image_54, (left, top))
    elif shape == IMAGE_55:
        display_surface.blit(image_55, (left, top))





def getShapeAndColor(board, boxx, boxy):
    # shape value for x, y spot is stored in board[x][y][0]
    # color value for x, y spot is stored in board[x][y][1]
    return board[boxx][boxy][0], board[boxx][boxy][1]


def drawBoxCovers(board, boxes, coverage):
    # Draws boxes being covered/revealed. "boxes" is a list
    # of two-item lists, which have the x & y spot of the box.
    for box in boxes:
        left, top = leftTopCoordsOfBox(box[0], box[1])
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (left, top, BOXSIZE, BOXSIZE))
        shape, color = getShapeAndColor(board, box[0], box[1])
        drawIcon(shape, color, box[0], box[1])
        if coverage > 0: # only draw the cover if there is an coverage
            pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, coverage, BOXSIZE))

    pygame.display.update()
    FPSCLOCK.tick(FPS)


def revealBoxesAnimation(board, boxesToReveal):
    # Do the "box reveal" animation.
    for coverage in range(BOXSIZE, (-REVEALSPEED) - 1, -REVEALSPEED):
        drawBoxCovers(board, boxesToReveal, coverage)

def coverBoxesAnimation(board, boxesToCover):
    # Do the "box cover" animation.
    for coverage in range(0, BOXSIZE + REVEALSPEED, REVEALSPEED):
        drawBoxCovers(board, boxesToCover, coverage)


def drawBoard(board, revealed):
    global Score, Time, output_time, message,level
    # Draws all of the boxes in their covered or revealed state.
    for boxx in range(BOARDWIDTH):
        for boxy in range(BOARDHEIGHT):
            left, top = leftTopCoordsOfBox(boxx, boxy)
            if not revealed[boxx][boxy]:
                # Draw a covered box.
                pygame.draw.rect(DISPLAYSURF, BOXCOLOR, (left, top, BOXSIZE, BOXSIZE))
                #   Draw Text View
                Score += 0
                font = pygame.font.Font('freesansbold.ttf', 32)
                # create a text suface object,
                # on which text is drawn on it.
                text = font.render('Score : ' + str(Score), True, WHITE, NAVYBLUE)
                time_text = font.render(output_time, True, WHITE, NAVYBLUE)
                message_text = font.render(message,True,RED,NAVYBLUE)
                level_text = font.render('Level ' + str(level), True, WHITE, NAVYBLUE)

                # create a rectangular object for the
                # text surface object
                textRect = text.get_rect()
                textTime = time_text.get_rect()
                textMessage = message_text.get_rect()
                textLevel = level_text.get_rect()

                # set the center of the rectangular object.
                textRect.center = (100, 775)
                textTime.center = (1080, 775)
                textMessage.center = (600, 775)
                textLevel.center = (600, 25)

                DISPLAYSURF.blit(text, textRect)
                DISPLAYSURF.blit(time_text, textTime)
                DISPLAYSURF.blit(message_text, textMessage)
                DISPLAYSURF.blit(level_text, textLevel)

            else:
                # Draw the (revealed) icon.
                shape, color = getShapeAndColor(board, boxx, boxy)
                drawIcon(shape, color, boxx, boxy)
def timer_manager():
    global timer, output_time, frame_rate, frame_count, runner, message, pause
    timer -= 1
    if(runner == True):
        if (timer > -1):
            threading.Timer(1.0, timer_manager).start()
            total_seconds = timer - (frame_count // frame_rate)
            if total_seconds < 0:
                total_seconds = 0

            # Divide by 60 to get total minutes
            minutes = total_seconds // 60

            # Use modulus (remainder) to get seconds
            seconds = total_seconds % 60
            output_time = "Time: {0:02}:{1:02}".format(minutes, seconds)
            message = ""
        else:
            message = "Time Is Over !"
            sys.exit(1)
    print(output_time)

def drawHighlightBox(boxx, boxy):
    left, top = leftTopCoordsOfBox(boxx, boxy)
    pygame.draw.rect(DISPLAYSURF, HIGHLIGHTCOLOR, (left - 5, top - 5, BOXSIZE + 10, BOXSIZE + 10), 4)

def startGameAnimation(board):

    # Randomly reveal the boxes 8 at a time.
    coveredBoxes = generateRevealedBoxesData(False)
    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))
    random.shuffle(boxes)
    boxGroups = splitIntoGroupsOf(8, boxes)

    drawBoard(board, coveredBoxes)
    for boxGroup in boxGroups:
        revealBoxesAnimation(board, boxGroup)
        coverBoxesAnimation(board, boxGroup)


def gameWonAnimation(board):
    global Score
    Score += 20
    # flash the background color when the player has won
    coveredBoxes = generateRevealedBoxesData(True)
    color1 = LIGHTBGCOLOR
    color2 = BGCOLOR

    for i in range(13):
        color1, color2 = color2, color1 # swap colors
        DISPLAYSURF.fill(color1)
        drawBoard(board, coveredBoxes)
        pygame.display.update()
        pygame.time.wait(300)


def hasWon(revealedBoxes):
    global Score
    # Returns True if all the boxes have been revealed, otherwise False
    for i in revealedBoxes:
        if False in i:
            Score += 20
            # print("Score : " + str(Score))
            return False  # return False if any boxes are covered.
    return True
if __name__ == '__main__':
    main()