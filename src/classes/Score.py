class Score:
    window = None
    score = 0

    def __init__(self, window):
        self.window = window

    def countPoints(self):
        self.score += 50
    
    def drawScore(self):
        self.window.draw_text("Points: " + str(self.score), (self.window.width / 2) - 50, 10, 20, (255, 255, 255), "Arial", True, False)
