import sys
import pygame
import util
from pygame.locals import *
from Dragon import *
SCREEN_WIDTH = 626
SCREEN_HEIGHT = 417

def game():
    pygame.init()
    X=100
    Y=100
    screen = pygame.display.set_mode((626, 417))
    pygame.display.set_caption("AnimacionAdapter")
    background_image = util.cargar_imagen('imagenes/Dragon/fondo.gif')
    pygame.mouse.set_visible(False)
    dr = Dragon()
    dr.Posic(X,Y)
    running = True
    playing = True 
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        screen.blit(background_image, (0,0))
        if playing:            
            dr.update(sprite)
            dr.draw(screen)
        pygame.display.update()  

if __name__ == '__main__':
    game()

