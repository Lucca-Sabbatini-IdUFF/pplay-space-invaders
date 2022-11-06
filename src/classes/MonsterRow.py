import math
import src.classes.Monster

class MonsterRow:
    window = None
    monsters = []

    def __init__(self, window, id, yPosition, rowParity):
        self.window = window
    
        self.id = id

        self.yPosition = yPosition

        monstersCount = math.floor((self.window.width) / 98)

        monsterSpace = self.window.width / monstersCount
        monsterIndex = 0

        for i in range(monstersCount):
          if (i == monstersCount - 1 and rowParity == 1):
            continue
          if (i % 2 == rowParity):
            self.monsters.append(src.classes.Monster.Monster(self.window, '{rowId}-{monsterId}'.format(rowId = self.id, monsterId = monsterIndex), ((i + 1) * monsterSpace - 49), yPosition, 25))
            monsterIndex += 1

    def moveDown(self, playerY):
        for monster in self.monsters:
            monster.moveDown()
            
            if monster.gameObject.y + monster.gameObject.height >= playerY:
                self.window.gameOver = True
                return