import math
import src.classes.MonsterRow

class MonsterGrid:
    window = None
    monsterRows = []

    def __init__(self, window):
        self.window = window

        monstersRowsCount = 3
        monsterSpace = 70
        monsterRowIndex = 0
        rowParity = 0

        for i in range(monstersRowsCount):
            self.monsterRows.append(src.classes.MonsterRow.MonsterRow(self.window, monsterRowIndex, (i + 1) * monsterSpace, rowParity))
            monsterRowIndex += 1
            if (rowParity == 1):
              rowParity = 0
            else:
              rowParity = 1

    def drawGrid(self):
        for row in self.monsterRows:
            for monster in row.monsters:
                monster.gameObject.draw()

    def checkCollisions(self, shots):
        for row in self.monsterRows:
            for monster in row.monsters:
                for shot in shots:
                    if (shot.gameObject.collided(monster.gameObject)):
                        row.monsters.remove(monster)
                        del monster

                        shots.remove(shot)
                        del shot

