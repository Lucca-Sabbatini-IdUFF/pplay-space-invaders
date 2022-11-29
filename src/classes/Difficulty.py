import src.classes.Button
import src.classes.MainMenu
import src.pplay.sprite


class Difficulty:
    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite(
            "./assets/images/difficulty_title.png")

        self.easyButton = src.classes.Button.Button(
            "./assets/images/difficulty_easy.png", 0, 0)
        self.normalButton = src.classes.Button.Button(
            "./assets/images/difficulty_normal.png", 0, 0)
        self.hardButton = src.classes.Button.Button(
            "./assets/images/difficulty_hard.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.easyButton.gameObject.x = (
            self.window.width / 2) - self.easyButton.gameObject.width / 2
        self.easyButton.gameObject.y = 200

        self.normalButton.gameObject.x = (
            self.window.width / 2) - self.normalButton.gameObject.width / 2
        self.normalButton.gameObject.y = 300

        self.hardButton.gameObject.x = (
            self.window.width / 2) - self.hardButton.gameObject.width / 2
        self.hardButton.gameObject.y = 400

    def drawScreen(self):
        self.title.draw()
        self.easyButton.gameObject.draw()
        self.normalButton.gameObject.draw()
        self.hardButton.gameObject.draw()

    def loop(self, clicked):
        self.drawScreen()

        if (self.mouse.is_over_object(self.easyButton.gameObject) and clicked):
            self.window.gameDifficulty = 1
            self.screen = src.classes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.normalButton.gameObject) and clicked):
            self.window.gameDifficulty = 1.5
            self.screen = src.classes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.hardButton.gameObject) and clicked):
            self.window.gameDifficulty = 2
            self.screen = src.classes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)

        if (self.keyboard.key_pressed("ESC")):
            self.screen = src.classes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
