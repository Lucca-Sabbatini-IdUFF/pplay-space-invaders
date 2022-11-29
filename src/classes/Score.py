class Score:
    def __init__(self, window):
        self.window = window
        self.score = 0

    def countPoints(self):
        self.score += 50

    def drawScore(self):
        self.window.draw_text("Points: " + str(self.score), (self.window.width /
                              2) - 50, 10, 20, (255, 255, 255), "Arial", True, False)
