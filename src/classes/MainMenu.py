import src.classes.Button
import src.classes.Game

class MainMenu:
    window = None
    mouse = None
    keyboard = None
    screen = None

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.playButton = src.classes.Button.Button("./assets/images/play_button.png", 10, 10)
        self.difficultyButton = src.classes.Button.Button("./assets/images/difficulty_button.png", 10, 160)
        self.rankingButton = src.classes.Button.Button("./assets/images/ranking_button.png", 10, 310)
        self.exitButton = src.classes.Button.Button("./assets/images/exit_button.png", 10, 460)

    def drawScreen(self):
        self.playButton.gameObject.draw()
        self.difficultyButton.gameObject.draw()
        self.rankingButton.gameObject.draw()
        self.exitButton.gameObject.draw()

    def loop(self):
        self.drawScreen()

        if (self.mouse.is_over_object(self.playButton.gameObject) and self.mouse.is_button_pressed(1)):
            self.screen = src.classes.Game.Game(self.window, self.mouse, self.keyboard)