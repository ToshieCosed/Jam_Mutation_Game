class TileMap():
    def __init__(self, width_x, width_y):
        self.width_x = width_x
        self.width_y = width_y
        self.map = [[0 for x in range(self.width_x)] for y in range(self.width_y)]

    def changetileat(self, tilenum, x, y):
        self.map[x][y] = tilenum

    def gettileat(self, x, y):
        return self.map[x][y]

