import pygame

class TileSystem():
    def make_tiles(self, tilesizex, tilesizey, surface):

        img = pygame.Surface.subsurface(surface, pygame.Rect( (0, 0), (32, 32) ))
        for x in range(0, 12):
            for y in range(0, 10):
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
        targetsurface.blit(self.tiles[tilenum], targetrect)




  
