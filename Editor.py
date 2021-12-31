import pygame
from pygame import mouse
import pygame.constants
from Sprite import Sprite
from Menus import Menus
from TileMap import TileMap
import math

import random

from TileSystem import TileSystem


pygame.init()
clock = pygame.time.Clock()

def DrawGrid():
    
    for i in range(0, 32):
        pygame.draw.line(screen, ([255, 0, 0]), (i *32, 0), (i*32, 768))
    for j in range(0, 32):
        pygame.draw.line(screen, ([255, 0, 0]), (0, j*32), (1024, j*32))


mouse_down_state = 0


screen_width = 1440
screen_height = 1024
screen_tiles_w = 32
screen_tiles_h = 32
#set screen
screen = pygame.display.set_mode([screen_width,screen_height], pygame.SCALED)

size = width, height = (32, 32)
s = pygame.Surface(size)
clear_screen = pygame.Surface([1440, 1024])
clear_screen.fill([0, 0, 0])

mouse_graphic = pygame.image.load('Assets/Mouse.png').convert()
toggle_grid = pygame.image.load('Assets/ToggleGrid_Editor.png').convert()


tilesystem = TileSystem()

#off by one would be 32, 24 but it needs one extra for the 0'th slot. -.-
tilesystem.make_tiles(33, 25, tilesystem.tiles_image)
tilemap = TileMap(33, 33)



color = [255, 255, 0]
s.fill(color)

screen.blit(s, [100, 100])
pygame.display.flip()

curtilenum = 1
drawgrid = 1

running = True

while(running):
    clock.tick(60)


    if mouse_down_state == 1:

        mxy = mouse.get_pos()
        
        mx = mxy[0]
        my = mxy[1]

        tilex_diff = math.floor((mx % 32))
        tiley_diff = math.floor((my %32))
        #get the tile placement location
        target_x = math.floor(mx / 32)
        target_y = math.floor(my / 32)

        if (target_x < 32):
            if (target_y <32):
                    #Another stupid catch because apparently out of range is somehow possible
                if (curtilenum <= len(tilesystem.tiles)):
                    tilemap.changetileat(curtilenum, target_x, target_y)


        #get editor tiles
        if (target_x >=32):
            if (target_y < 24):
                tx = target_x - 32
                ty = target_y

                curtilenum = math.floor( (ty* 13) + tx)
                if curtilenum > 130:
                    curtilenum = 130
                    #print(curtilenum)



    screen.blit(clear_screen, [0,0])


    #print(len(tilesystem.tiles))

    for i in range(0, 32):
        for j in range(0, 32):
            l = 1
            if (tilemap.gettileat(i, j)) !=None:
                l = tilemap.gettileat(i, j)

            tilesystem.drawtileat(screen, i, j, l)


    #draw tileset
    tilesystem.draw_tilesetat(screen, 1024, 0)

    #draw grid if grid is on
    if drawgrid == 1:
        DrawGrid()

    #draw currently selected tile
    tilesystem.drawtileat(screen,34,20, curtilenum)

    #draw buttons and whatnot
    screen.blit(toggle_grid, (32* 35, 22 * 32))
    

    #screen.blit(mouse_graphic, (mx, my))
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # It's still wise to be able to close your program.
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
           mouse_down_state = 1
           #Dealing with a gui button to turn on /off grid
           startx = (32* 35)
           starty = (22* 32)
           endx = startx + 64
           endy = starty + 46
           toggled = 0

           mxy = mouse.get_pos()
           mx = mxy[0]
           my = mxy[1]


           if (mx > startx):
               if (mx < endx):
                   if (my > starty):
                        if (my <endy):
                            if drawgrid == 1: 
                                drawgrid = 0
                                toggled = 1
                            if toggled == 0:
                                if drawgrid == 0:
                                    drawgrid = 1



        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down_state = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tilemap.save_map()
            
            if event.key == pygame.K_l:
                tilemap.load_map()


                


  
