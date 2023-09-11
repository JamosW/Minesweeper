#1- Import packages
import sys
from ButtonManager import *
from pygwidgets import TextButton


# 2 - Define constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 480
FRAMES_PER_SECOND = 100


# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

# 4 - Load assets: image(s), sound(s), etc.
random.choice([1,2])

# 5 - Initialize variables
outerBox = pygame.Rect(-2 + OUTERBOX_OFFSET/2, 0 + 30, WINDOW_WIDTH - OUTERBOX_OFFSET + 4,  WINDOW_HEIGHT - 53)
oManager = ButtonManager(window, outerBox=outerBox)
oButton = TextButton(window, (620, 70), "Restart", 60, 40)

# 6 - Loop forever
while True:
  
  #7 - Check for and handlel events
    for event in pygame.event.get():
        # Clicked the close button? Quit pygame and end the program
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        oManager.handleEvent(event)
        oManager.checkForBomb()
        if oButton.handleEvent(event):
          oManager = ButtonManager(window, outerBox=outerBox)

        
  # 8 - Do any "per frame" actions
    
  # 9 - Clear the window
    window.fill(pygame.Color("white"))
      
      
  # 10 - Draw all window elements
    pygame.draw.rect(window, "azure4", outerBox)

    oManager.draw()
    oButton.draw()
    
  # 11 - Update the window
    pygame.display.update()
    
  # 12 - Slow things down a bit
