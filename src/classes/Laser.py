from src.pplay.sprite import *


class Laser:
    def __init__(self, window, initialSpeed, shooter):
        self.window = window
        self.shooter = shooter
        self.gameObject = Sprite("./assets/images/laser_red.png", 1)

        self.gameObject.x = self.shooter.gameObject.x + \
            (self.shooter.gameObject.width / 2) - self.gameObject.width / 2
        self.gameObject.y = self.shooter.gameObject.y - self.gameObject.height

        self.absoluteSpeed = initialSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed

    def moveUp(self):
        self.gameObject.y -= self.ySpeed * self.window.delta_time()

        if (self.gameObject.y < 0):
            return False

        return True
