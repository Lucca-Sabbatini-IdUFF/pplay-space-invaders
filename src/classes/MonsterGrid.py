import math
import src.classes.MonsterRow

class MonsterGrid:
    window = None
    monsterRows = []
    orientation = True

    def __init__(self, window):
        self.window = window

        monstersRowsCount = 3
        monsterSpace = 70
        monsterRowIndex = 0
        rowParity = 0

        for i in range(monstersRowsCount):
            self.monsterRows.append(src.classes.MonsterRow.MonsterRow(self.window, monsterRowIndex, (i + 1) * monsterSpace, rowParity))
            monsterRowIndex += 1
            # rowParity = not rowParity # If uncommented, monster alignment is alternated

    def drawGrid(self, playerY):
        for row in self.monsterRows:
            for monster in row.monsters:
                monster.gameObject.draw()
                newOrientation = monster.move(self.orientation)
                if newOrientation != self.orientation:
                    self.orientation = newOrientation
                    row.moveDown(playerY)

    def checkCollisions(self, shots):
        for row in self.monsterRows:
            for monster in row.monsters:
                for shot in shots:
                    if (shot.gameObject.collided(monster.gameObject)):
                        row.monsters.remove(monster)
                        del monster

                        shots.remove(shot)
                        del shot

