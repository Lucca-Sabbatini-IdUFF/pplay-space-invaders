from src.pplay.sprite import *

class Monster:
    window = None
    gameObject = None
    id = None
    absoluteSpeed = None
    ySpeed = None
    orientation = True

    def __init__(self, window, id, xPosition, yPosition, initialSpeed):
        self.window = window
        self.gameObject = Sprite("./assets/images/enemy_ship.png", 1)

        self.id = id
    
        self.gameObject.x = xPosition
        self.gameObject.y = yPosition

        self.absoluteSpeed = initialSpeed
        self.xSpeed = self.absoluteSpeed
        self.ySpeed = self.gameObject.height
    
    def moveDown(self):
        self.gameObject.y += self.ySpeed

        if (self.gameObject.y < self.window.height):
            return False

        return True

    def moveLeft(self, orientation):
        self.gameObject.x -= self.xSpeed * self.window.delta_time()
        if (self.gameObject.x < 0):
            self.gameObject.x = 0            
            return not orientation 
        return orientation 

    def moveRight(self, orientation):
        self.gameObject.x += self.xSpeed * self.window.delta_time()
        if (self.gameObject.x > self.window.width - self.gameObject.width):
            self.gameObject.x = self.window.width - self.gameObject.width
            return not orientation
        return orientation       
    
    def move(self, orientation):
        if orientation:
            return self.moveRight(orientation)
        elif not orientation:
            return self.moveLeft(orientation)

        