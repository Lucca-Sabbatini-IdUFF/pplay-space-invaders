from src.pplay.sprite import *

class Monster:
    window = None
    gameObject = None
    id = None
    absoluteSpeed = None
    ySpeed = None

    def __init__(self, window, id, xPosition, yPosition, initialSpeed):
        self.window = window
        self.gameObject = Sprite("./assets/images/enemy_ship.png", 1)

        self.id = id
    
        self.gameObject.x = xPosition
        self.gameObject.y = yPosition

        self.absoluteSpeed = initialSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.absoluteSpeed
    
    def moveDown(self):
        self.gameObject.y += self.ySpeed * self.window.delta_time()

        if (self.gameObject.y < self.window.height):
            return False

        return True

    def moveLeft(self):
        self.gameObject.x -= self.xSpeed * self.window.delta_time()
        if (self.gameObject.x < 20):
            self.gameObject.x = 20

    def moveRight(self):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        if (self.gameObject.x > self.window.width - self.gameObject.width - 20):
            self.gameObject.x = self.window.width - self.gameObject.width - 20