import src.classes.Button
import src.classes.Player
import src.classes.MonsterGrid
import src.classes.MainMenu
import src.classes.Score
import src.classes.HUD


class Game:
    reset = False
    initialMonsterSpeed = 30

    def __init__(self, window, mouse, keyboard):
        self.window = window
        self.mouse = mouse
        self.keyboard = keyboard
        self.screen = self
        self.player = src.classes.Player.Player(window, keyboard)
        self.score = src.classes.Score.Score(self.window)
        self.hud = src.classes.HUD.HUD(self.window, self.player)
        self.monster_grid = src.classes.MonsterGrid.MonsterGrid(
            self.window, self.score, self.initialMonsterSpeed * self.window.gameDifficulty)

    def drawScreen(self):
        self.score.drawScore()
        self.hud.draw_hud()
        self.player.gameObject.draw()
        self.monster_grid.drawGrid(self.player.gameObject.y)

    def loop(self, click):
        self.drawScreen()
        self.player.control()
        self.player.shotCooldownCheck(self.window.delta_time())
        self.monster_grid.checkCollisions(self.player.shots)

        if (not self.window.gameOver and (self.monster_grid.get_alive_monsters_count() == 0)):
            self.monster_grid.monsterRows = []
            self.window.gameDifficulty += 0.1
            self.monster_grid = src.classes.MonsterGrid.MonsterGrid(
                self.window, self.score, self.initialMonsterSpeed * self.window.gameDifficulty)

        if (self.keyboard.key_pressed("ESC") or self.window.gameOver):
            self.window.gameOver = False
            self.monster_grid = None
            self.screen = src.classes.MainMenu.MainMenu(
                self.window, self.mouse, self.keyboard)
