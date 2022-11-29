from src.pplay.sprite import *
import src.classes.Laser


class Player:
    absoluteSpeed = 400
    moveLeftKeybind = "LEFT"
    moveRightKeybind = "RIGHT"
    shootLaserKeybind = "SPACE"
    shotSpeed = 600

    def __init__(self, window, keyboard):
        self.window = window
        self.keyboard = keyboard
        self.gameObject = Sprite("./assets/images/player.png", 1)
        self.lives = 3

        self.shotCooldownAbsolute = 0.6
        self.shotCooldown = 0
        self.shots = []

        self.gameObject.x = (self.window.width / 2) - \
            (self.gameObject.width / 2)
        self.gameObject.y = (self.window.height) - \
            (self.gameObject.height) - 20

        self.absoluteSpeed = self.absoluteSpeed
        self.xSpeed = self.absoluteSpeed

    def take_hit(self):
        self.lives -= 1

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
        self.shots.append(src.classes.Laser.Laser(
            self.window, self.shotSpeed, self))

    def shotCooldownCheck(self, timePassed):
        self.shotCooldown -= timePassed
        if (self.shotCooldown < 0):
            self.shotCooldown = 0
