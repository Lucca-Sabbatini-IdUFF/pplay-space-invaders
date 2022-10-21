from src.pplay.sprite import *
import src.classes.Laser

class Player:
    window = None
    keyboard = None
    gameObject = None
    absoluteSpeed = 400
    xSpeed = None
    moveLeftKeybind = "LEFT"
    moveRightKeybind = "RIGHT"
    shootLaserKeybind = "SPACE"
    shotSpeed = 600
    shotCooldownAbsolute = None
    shotCooldown = 0
    shots = []

    def __init__(self, window, keyboard):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/player.png", 1)

        self.shotCooldownAbsolute = 0.3 + (0.3 * self.window.gameDifficulty)

        self.gameObject.x = (self.window.width / 2) - (self.gameObject.width / 2)
        self.gameObject.y = (self.window.height) - (self.gameObject.height) - 20

        self.absoluteSpeed = self.absoluteSpeed / self.window.gameDifficulty
        self.xSpeed = self.absoluteSpeed

        self.shotSpeed = self.shotSpeed / self.window.gameDifficulty

        print(self.shotCooldownAbsolute)

    def control(self):        
        if (self.keyboard.key_pressed(self.shootLaserKeybind) and (self.shotCooldown == 0)):
            self.shoot()

        if (self.keyboard.key_pressed(self.moveLeftKeybind) and self.gameObject.x > 0):
            self.moveLeft()

        if (self.keyboard.key_pressed(self.moveRightKeybind) and self.gameObject.x < (self.window.width - self.gameObject.width)):
            self.moveRight()

        for shot in self.shots:
            shot.gameObject.draw()
            isInBounds = shot.moveUp()

            if (not isInBounds):
                self.shots.remove(shot)
                del shot

    def moveLeft(self):
        self.gameObject.x -= self.xSpeed * self.window.delta_time()
        if (self.gameObject.x < 20):
            self.gameObject.x = 20

    def moveRight(self):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        if (self.gameObject.x > self.window.width - self.gameObject.width - 20):
            self.gameObject.x = self.window.width - self.gameObject.width - 20

    def shoot(self):
        self.shotCooldown = self.shotCooldownAbsolute
        self.shots.append(src.classes.Laser.Laser(self.window, self.shotSpeed, self))

    def shotCooldownCheck(self, timePassed):
        self.shotCooldown -= timePassed
        if (self.shotCooldown < 0):
            self.shotCooldown = 0
