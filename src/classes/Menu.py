from src.classes.Button import *

class Menu:
    window = None

    def __init__(self, window):
        self.window = window

        self.playButton = Button("./assets/images/play_button.png", 10, 10)
        self.difficultyButton = Button("./assets/images/difficulty_button.png", 10, 160)
        self.rankingButton = Button("./assets/images/ranking_button.png", 10, 310)
        self.exitButton = Button("./assets/images/exit_button.png", 10, 460)

    def drawScreen(self):
        self.playButton.gameObject.draw()
        self.difficultyButton.gameObject.draw()
        self.rankingButton.gameObject.draw()
        self.exitButton.gameObject.draw()