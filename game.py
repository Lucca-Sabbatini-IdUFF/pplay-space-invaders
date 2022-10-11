# Imports
from src.pplay.window import *
import src.classes.MainMenu

# Game Window Initialization
gameWindow = Window(1200,600)
gameWindow.set_title("Space Invaders")

# Controls Initialization
keyboard = gameWindow.get_keyboard()
mouse = gameWindow.get_mouse()

# Initialize Screen
currentScreen = src.classes.MainMenu.MainMenu(gameWindow, mouse, keyboard)

# Game Loop
while (gameWindow):
    # Clean Background
    gameWindow.set_background_color((0, 0, 0))
    
    currentScreen.loop()
    currentScreen = currentScreen.screen

    # Update Window
    gameWindow.update()