import math
import src.classes.Monster


class MonsterRow:
    def __init__(self, window, id, yPosition, rowParity, initialSpeed):
        self.window = window
        self.id = id
        self.yPosition = yPosition
        self.monsters = []

        # Represents twice of the monster count
        monstersCount = math.floor((self.window.width) / 98)
        monsterSpace = self.window.width / monstersCount
        monsterIndex = 0

        for i in range(monstersCount):
            if ((i == monstersCount - 1 and rowParity == 1) or (i == monstersCount - 1) or (i == 0)):
                continue
            if (i % 2 == rowParity):
                self.monsters.append(src.classes.Monster.Monster(self.window, '{rowId}-{monsterId}'.format(
                    rowId=self.id, monsterId=monsterIndex), ((i + 1) * monsterSpace - 49), yPosition, initialSpeed))
                monsterIndex += 1

    def moveDown(self, playerY):
        for monster in self.monsters:
            monster.moveDown()

            if monster.gameObject.y + monster.gameObject.height >= playerY:
                self.window.gameOver = True
                return
