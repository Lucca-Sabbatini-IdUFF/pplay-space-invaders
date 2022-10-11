import src.classes.Button
import src.classes.MainMenu

class Game:
    window = None
    mouse = None
    keyboard = None
    screen = None

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

    def drawScreen(self):
        return

    def loop(self, click):
        self.drawScreen()

        if (self.keyboard.key_pressed("ESC")):
            self.screen = src.classes.MainMenu.MainMenu(self.window, self.mouse, self.keyboard)
