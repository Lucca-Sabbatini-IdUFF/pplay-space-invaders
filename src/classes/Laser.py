from src.pplay.sprite import *

class Laser:
    window = None
    gameObject = None
    absoluteSpeed = None
    ySpeed = None

    def __init__(self, window, initialSpeed, player):
        self.window = window
        self.player = player
        self.gameObject = Sprite("./assets/images/laser_red.png", 1)
    
        self.gameObject.x = self.player.gameObject.x + (self.player.gameObject.width / 2) - self.gameObject.width / 2
        self.gameObject.y = self.player.gameObject.y - self.gameObject.height

        self.absoluteSpeed = initialSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed
    
    def moveUp(self):
        self.gameObject.y -= self.ySpeed * self.window.delta_time()

        if (self.gameObject.y < 0):
            return False

        return True