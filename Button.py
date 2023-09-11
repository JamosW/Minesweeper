import pygame
from pygame.locals import *

class Button():
    
    __slots__ = ["window", "maxWidth", "maxHeight", "x", "y", "hasBomb", "buttonRect", "flagged", "bottomImg", "topImg", "currentImg", "rightClicked", "leftClicked", "ID","buttonDownImg", "freeToClear"]
    
    def __init__(self, window, windowWidth, windowHeight, x, y, hasBomb, buttonWidth, buttonHeight, bottomImg, topImg, ID, buttonDownImg):
        self.window = window
        self.maxWidth = windowWidth
        self.maxHeight = windowHeight
        self.x = x
        self.y = y
        self.buttonRect = pygame.Rect(self.x, self.y, buttonWidth, buttonHeight)
        self.hasBomb = hasBomb
        self.bottomImg = bottomImg
        self.topImg = topImg
        self.currentImg = topImg
        self.buttonDownImg = buttonDownImg
        self.ID = ID
        
        self.rightClicked= False
        #clicking on tile is two step process, button down and button up
        self.leftClicked = [False, False]
        self.flagged = False
        self.freeToClear = True
        
    
    #perhaps temprary
    def handleEvent(self, event):
        if not(all(self.leftClicked)):
                    self.currentImg = self.topImg
            
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1 and self.buttonRect.collidepoint(event.pos):
                self.leftClicked[0] = True
                self.currentImg = self.buttonDownImg
            if event.button == 3 and self.buttonRect.collidepoint(event.pos):
                self.flagged = not(self.flagged)
                if self.flagged:
                    self.freeToClear = False
                self.rightClicked = True
        if event.type == MOUSEBUTTONUP:
            if event.button == 1 and self.buttonRect.collidepoint(event.pos):
                self.leftClicked[1] = True
        
        
                    

        
    def draw(self):
            self.window.blit(self.currentImg, self.buttonRect)
            
            
        