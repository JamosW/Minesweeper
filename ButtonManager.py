from Button import *
import random
from constants import *
from numpy import array, isin, logical_not
from numpy.random import choice
from pygame.locals import *

class ButtonManager():
    
    WIDTH = 15
    HEIGHT = 15
    BUTTONS_PER_COLUMN = 25
    ROW_SPACING = 17
    BUTTONS_PER_ROW = 30
    spriteSheetImage = pygame.image.load("images/minesweeper_tiles.jpeg")
    
    
    def __init__(self, window, outerBox):
        
        self.imageList = []
        self.spriteSheetImage = pygame.Surface.convert(ButtonManager.spriteSheetImage)
        self.updateImageList(12, 128, 128)
        self.tileImg, self.flagImg, self.bombImg, self.emptyImg, self.oneImg, self.twoImg, self.threeImage, self.fourImage, self.fiveImage, self.sixImage, self.sevenImg, self.eightImage =  [img for img in self.imageList]
        
        self.window = window
        self.buttonRow = [(i * ButtonManager.WIDTH ) + (2 * i) + OUTERBOX_OFFSET/2 for i in range(ButtonManager.BUTTONS_PER_ROW)]
        self.buttonList = [Button(window, outerBox.width, outerBox.height, x=row, y=(col * 17) + 32, hasBomb=choice([True, False], p = [0.15, 0.85]), buttonWidth=ButtonManager.WIDTH, buttonHeight=ButtonManager.HEIGHT, bottomImg=None, topImg=self.tileImg, ID=(((array(row) - 66) / 17) + 1) + (col * 30), buttonDownImg=self.emptyImg) for row in self.buttonRow for col in range(ButtonManager.BUTTONS_PER_COLUMN)]
        self.triggered = False
        self.bombsList = array([array([button.x, button.y]) for button in self.buttonList if button.hasBomb])
        self.giveIcons()

                
    def handleEvent(self, event):
        for button in self.buttonList:
            if not(self.triggered):
                button.handleEvent(event)
                       
    def checkForBomb(self):
        for button in self.buttonList:
            if all(button.leftClicked) and button.hasBomb:
                self.triggered = True
        
    def draw(self):
        for button in self.buttonList:
            
            if self.triggered:
                if button.hasBomb:
                    button.currentImg = self.bombImg
            else:
                if all(button.leftClicked):
                    button.currentImg = button.bottomImg
                    if button.bottomImg == self.emptyImg:
                        self.clearOut(button)        
                elif button.rightClicked:
                    if not(all(button.leftClicked)) and button.flagged:
                        button.currentImg = self.flagImg
                    elif not(all(button.leftClicked)) and not(button.flagged):
                        button.currentImg = self.tileImg
            
            button.draw()

                
    def updateImageList(self, nImages, width, height):
        nCols = self.spriteSheetImage.get_width()
        
        row = 0
        col = 0
        for imageNumber in range(nImages):
            x = row * width
            y = col * height
            
            subRect = pygame.Rect(x,y, width, height)
            image = self.spriteSheetImage.subsurface(subRect)
            image = pygame.transform.scale(image, (ButtonManager.WIDTH, ButtonManager.HEIGHT))
            self.imageList.append(image)
            
            row += 1
            if x == (nCols - width):
                row =  0
                col = col + 1
        
    def giveIcons(self):
        for button in self.buttonList:
            button.bottomImg = self.imageList[3 + len([pair for pair in self.bombsList - array([button.x, button.y]) if (sum(abs(pair)) <= 34) & logical_not(isin(34, abs(pair)))])]
        
                
    def clearOut(self, btn):
        
        for button in self.buttonList:
            #If up, right, left or down
            if not(button.flagged):
                #if button.rightClicked and adjacent button is not(leftClicked)
                #pair = array([button.x, button.y])
                
                if(
                #Up
                ((btn.x + 17) == button.x) and btn.y == button.y or 
                #Down
                ((btn.y + 17) == button.y) and btn.x == button.x or 
                #Left
                ((btn.x - 17) == button.x) and btn.y == button.y or 
                #Right
                ((btn.y - 17) == button.y) and btn.x == button.x or 
                #diag right - up
                ((btn.x + 17) == button.x) and (btn.y - 17) == button.y or
                #diag right down
                ((btn.x + 17) == button.x) and (btn.y + 17) == button.y or
                #diag left up
                ((btn.x - 17) == button.x) and (btn.y - 17) == button.y or
                #diag left down
                ((btn.x - 17) == button.x) and (btn.y + 17) == button.y):
                    button.leftClicked = [True, True]