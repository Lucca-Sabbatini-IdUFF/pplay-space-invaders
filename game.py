# Imports
import pygame
from pygame.locals import *
from src.pplay.window import *
import src.classes.MainMenu

# Initializes pygame's modules
pygame.init()
clock = pygame.time.Clock()

# Game Window Initialization
gameWindow = Window(1200,600)
gameWindow.set_title("Space Invaders")
gameWindow.gameDifficulty = 1

# Controls Initialization
keyboard = gameWindow.get_keyboard()
mouse = gameWindow.get_mouse()
rightClicking = False

# Initialize Screen
currentScreen = src.classes.MainMenu.MainMenu(gameWindow, mouse, keyboard)

# Game Loop
while (gameWindow):
    # Clean Background
    gameWindow.set_background_color((0, 0, 0))
    
    # Current Screen Game Loop
    currentScreen.loop(rightClicking)

    # Get Next Screen
    currentScreen = currentScreen.screen

    rightClicking = False

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                rightClicking = True
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                rightClicking = False

    # Update Window
    gameWindow.update()
    clock.tick(60)