import src.classes.MonsterRow
import src.classes.Laser

class MonsterGrid:
    shotSpeed = 600

    def __init__(self, window, score, initialSpeed):
        self.window = window
        self.score = score
        self.monsterRows = []
        self.orientation = True

        self.shotCooldownAbsolute = 0.6
        self.shotCooldown = 0
        self.shots = []

        monstersRowsCount = 3
        monsterSpace = 70
        monsterRowIndex = 0
        rowParity = 0

        for i in range(monstersRowsCount):
            self.monsterRows.append(src.classes.MonsterRow.MonsterRow(
                self.window, monsterRowIndex, (i + 1) * monsterSpace, rowParity, initialSpeed))
            monsterRowIndex += 1
            # rowParity = not rowParity  # If uncommented, monster alignment is alternated

    def shoot(self):
        self.shotCooldown = self.shotCooldownAbsolute
        self.shots.append(src.classes.Laser.Laser(
            self.window, self.shotSpeed, self))

    def shotCooldownCheck(self, timePassed):
        self.shotCooldown -= timePassed
        if (self.shotCooldown < 0):
            self.shotCooldown = 0

    def drawGrid(self, playerY):
        for row in self.monsterRows:
            for monster in row.monsters:
                monster.gameObject.draw()
                newOrientation = monster.move(self.orientation)
                if newOrientation != self.orientation:
                    self.orientation = newOrientation
                    self.moveRowsDown(playerY)

    def checkCollisions(self, shots):
        for row in self.monsterRows:
            for monster in row.monsters:
                for shot in shots:
                    if (shot.gameObject.collided(monster.gameObject)):
                        self.score.countPoints()

                        row.monsters.remove(monster)
                        del monster

                        shots.remove(shot)
                        del shot

    def get_alive_monsters_count(self):
        count = 0

        for row in self.monsterRows:
            count += len(row.monsters)

        return count

    def moveRowsDown(self, playerY):
        for row in self.monsterRows:
            row.moveDown(playerY)
