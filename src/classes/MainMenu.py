import sys
import src.classes.Button
import src.classes.Game
import src.classes.Difficulty
import src.classes.Score

class MainMenu:
    window = None
    mouse = None
    keyboard = None
    screen = None
    score = None

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.score = src.classes.Score.Score(self.window)

        self.title = src.pplay.sprite.Sprite("./assets/images/space_invaders_logo.png")

        self.playButton = src.classes.Button.Button("./assets/images/play_button.png", 0, 0)
        self.difficultyButton = src.classes.Button.Button("./assets/images/difficulty_button.png", 0, 0)
        self.rankingButton = src.classes.Button.Button("./assets/images/ranking_button.png", 0, 0)
        self.exitButton = src.classes.Button.Button("./assets/images/exit_button.png", 0, 0)

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

        self.playButton.gameObject.x = (self.window.width / 2) - self.playButton.gameObject.width / 2
        self.playButton.gameObject.y = 200

        self.difficultyButton.gameObject.x = (self.window.width / 2) - self.difficultyButton.gameObject.width / 2
        self.difficultyButton.gameObject.y = 300

        self.rankingButton.gameObject.x = (self.window.width / 2) - self.rankingButton.gameObject.width / 2
        self.rankingButton.gameObject.y = 400

        self.exitButton.gameObject.x = (self.window.width / 2) - self.exitButton.gameObject.width / 2
        self.exitButton.gameObject.y = 500

    def drawScreen(self):
        self.title.draw()
        self.playButton.gameObject.draw()
        self.difficultyButton.gameObject.draw()
        self.rankingButton.gameObject.draw()
        self.exitButton.gameObject.draw()

    def loop(self, clicked):
        self.drawScreen()

        if (self.mouse.is_over_object(self.playButton.gameObject) and clicked):
            self.screen = src.classes.Game.Game(self.window, self.mouse, self.keyboard, self.score)

        if (self.mouse.is_over_object(self.difficultyButton.gameObject) and clicked):
            self.screen = src.classes.Difficulty.Difficulty(self.window, self.mouse, self.keyboard)

        if (self.mouse.is_over_object(self.exitButton.gameObject) and clicked):
            sys.exit()