import src.components.Button
import src.screens.MainMenu
import src.pplay.sprite


class Ranking:
    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self

        self.title = src.pplay.sprite.Sprite(
            "./assets/images/ranking_title.png")

        self.title.x = (self.window.width / 2) - self.title.width / 2
        self.title.y = 50

    def draw_screen(self):
        self.title.draw()

    def loop(self, click):
        self.draw_screen()

        if self.keyboard.key_pressed("ESC"):
            self.screen = src.screens.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
