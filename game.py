import pygame

pygame.init()

screen_width = 1024
screen_height = 768
#set screen
screen = pygame.display.set_mode([screen_width,screen_height])

size = width, height = (32, 32)
s = pygame.Surface(size)


color = [255, 255, 0]
s.fill(color)

screen.blit(s, [100, 100])
pygame.display.flip()

running = True

while(running):

    screen.blit(s, [100, 100])
    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # It's still wise to be able to close your program.
            raise SystemExit

  
