import json

class TileMap():
    def __init__(self, width_x, width_y):
        self.width_x = width_x
        self.width_y = width_y
        self.map = [[0 for x in range(self.width_x)] for y in range(self.width_y)]

        for i in range(len(self.map)):
            for j in range(len(self.map[0])):
                self.map[i][j] = 1

    def changetileat(self, tilenum, x, y):
        self.map[x][y] = tilenum

    def gettileat(self, x, y):
        return self.map[x][y]

    def save_map(self):
        file = open('Assets/Templates/dump.json', 'w+')
        data = self.map
        json.dump(data, file)

    def load_map(self):
        file = open('Assets/Templates/dump.json', 'r+')
        self.map = json.load(file)