class HUD:
    def __init__(self, window, player):
        self.window = window
        self.player = player

    def draw_hud(self):
        self.window.draw_text("Lives: " + str(self.player.lives),
                              10, 10, 20, (255, 255, 255), "Arial", True, False)
