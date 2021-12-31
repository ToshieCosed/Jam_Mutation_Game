import json

class TileMap():
    def __init__(self, width_x, width_y):
        self.width_x = width_x
        self.width_y = width_y
        self.map = [[0 for x in range(self.width_x)] for y in range(self.width_y)]
        self.enemies = [("blank", 0, 0)]

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                self.map[i][j] = 0

    def changetileat(self, tilenum, x, y):
        self.map[x][y] = tilenum

    def gettileat(self, x, y):
        return self.map[x][y]

    def save_map(self):
        file = open('Assets/Templates/dump.json', 'w+')
        enemyfile = open('Assets/Templates/enemy.json', 'w+')
        data = self.map
        json.dump(data, file)
        enemydata = self.enemies
        json.dump(enemydata, enemyfile)

    def load_map(self):
        file = open('Assets/Templates/dump.json', 'r+')
        enemyfile = open('Assets/Templates/enemy.json', 'r+')
        self.map = json.load(file)
        self.enemies = json.load(enemyfile)

    def addenemyat(self, enemytype, x, y):
        self.enemies.append((enemytype, x, y))

    def removeenemyat(self, x, y):
        remove_ = None
        for e in self.enemies:
            x_ = e[1]
            y_ = e[2]
            if x_ == x:
                if y_ == y:
                    remove_ = e
                    break
        
        if remove_ != None:
            self.enemies.remove(e)

