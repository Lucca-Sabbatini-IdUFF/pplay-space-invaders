# Imports
from src.pplay.window import *
from src.classes.Menu import *

# Game Window Initialization
gameWindow = Window(1200,600)
gameWindow.set_title("Space Invaders")

# Controls Initialization
keyboard = gameWindow.get_keyboard()
mouse = gameWindow.get_mouse()

# Screens
menuScreen = Menu(gameWindow)


currentScreen = menuScreen

# Game Loop
while (gameWindow):
    # Clean Background
    gameWindow.set_background_color((0, 0, 0))
    
    if (currentScreen):
        currentScreen.drawScreen()

    # Update Window
    gameWindow.update()