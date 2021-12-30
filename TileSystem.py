import pygame

class TileSystem():
    def make_tiles(self, tilesizex, tilesizey, surface):

        img = pygame.Surface.subsurface(surface, pygame.Rect( (0, 0), (32, 32) ))
        for y in range(0, 10):
            for x in range(0, 13):
                targx = x*32
                targy = y*32
                targrect = pygame.Rect( (targx, targy), (32, 32))
                surf = pygame.Surface.subsurface(surface, targrect)
                self.tiles.append(surf)

    def __init__(self):
        self.tiles_image = pygame.image.load('Assets/Tiles.png')
        self.tiles_image.set_colorkey((239, 88, 252))
        
        #print(self.tiles_image.get_size() )
        self.tiles = []
    
    def drawtileat(self, targetsurface, tilex, tiley, tilenum):
        targetrect = pygame.Rect( ( tilex*32, tiley*32), (32, 32))
        length_ = len(self.tiles)
            #Should never be out of range but here's a catch. Whatever.
        if (tilenum <=length_-1):
            targetsurface.blit(self.tiles[tilenum], targetrect)
    
    def draw_tilesetat(self, targetsurface, startx, starty):
        targetrect = pygame.Rect( (startx, starty), (self.tiles_image.get_width(), self.tiles_image.get_height()))
        targetsurface.blit(self.tiles_image, targetrect)
        




  
