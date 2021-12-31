import pygame

class Text_Renderer():

    def __init__(self, targetsurface):

        pygame.font.init()
        self.renderfont = pygame.font.SysFont("Arial", 16)
        self.text = None

    def Print(self, targetsurface, input_string, offsetx, offsety):
        text = self.renderfont.render(input_string, True, (255, 255, 255))
        targetsurface.blit(text, (offsetx, offsety))


 

