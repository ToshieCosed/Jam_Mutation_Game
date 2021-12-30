import pygame
import pygame.constants
from Sprite import Sprite
from Menus import Menus
from TileMap import TileMap

import random

from TileSystem import TileSystem


pygame.init()
clock = pygame.time.Clock()


screen_width = 1024
screen_height = 768
screen_tiles_w = 32
screen_tiles_h = 24
#set screen
screen = pygame.display.set_mode([screen_width,screen_height])

size = width, height = (32, 32)
s = pygame.Surface(size)
clear_screen = pygame.Surface([1024, 768])
clear_screen.fill([0, 0, 0])

mouse_graphic = pygame.image.load('Assets/Mouse.png').convert()

tilesystem = TileSystem()
tilesystem.make_tiles(32, 32, tilesystem.tiles_image)



color = [255, 255, 0]
s.fill(color)

screen.blit(s, [100, 100])
pygame.display.flip()

running = True

while(running):
    clock.tick(1)

    screen.blit(clear_screen, [0,0])


    print(len(tilesystem.tiles))

    for i in range(0, 32):
        for j in range(0, 24):
            l = random.randrange(1, 50)
            tilesystem.drawtileat(screen, i, j, l)


    for i in range(0, 32):
        pygame.draw.line(screen, ([255, 0, 0]), (i *32, 0), (i*32, 768))
    for j in range(0, 24):
        pygame.draw.line(screen, ([255, 0, 0]), (0, j*32), (1024, j*32))

    xy =  pygame.mouse.get_pos()
    mx = xy[0]
    my = xy[1]

    screen.blit(mouse_graphic, (mx, my))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # It's still wise to be able to close your program.
            raise SystemExit

  
