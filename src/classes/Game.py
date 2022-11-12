import src.classes.Button
import src.classes.Player
import src.classes.MonsterGrid
import src.classes.MainMenu

class Game:
    window = None
    mouse = None
    keyboard = None
    screen = None
    playerSpeed = None
    score = None
    reset = False

    def __init__(self, window, mouse, keyboard, score):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.Player.Player(window, keyboard)
        self.score = score
        self.monsterGrid = src.classes.MonsterGrid.MonsterGrid(self.window, self.score)

    def drawScreen(self):
        self.score.drawScore()
        self.player.gameObject.draw()
        self.monsterGrid.drawGrid(self.player.gameObject.y)

    def loop(self, click):
        self.drawScreen()
        self.player.control()
        self.player.shotCooldownCheck(self.window.delta_time())
        self.monsterGrid.checkCollisions(self.player.shots)

        if (self.keyboard.key_pressed("ESC") or self.window.gameOver):
            self.window.gameOver = False
            self.screen = src.classes.MainMenu.MainMenu(self.window, self.mouse, self.keyboard)
