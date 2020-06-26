import sys
import pygame
import util
from adapter import Adaptador
from pygame.locals import *
from PJ import *

def game():
    pygame.init()
    screen = pygame.display.set_mode((626, 417))
    pygame.display.set_caption("adapter")
    inicio_image = util.cargar_imagen('imagenes/Dragon/fondo.gif')
    screen.blit(inicio_image, (0, 0))
    pygame.mouse.set_visible(False)
    ejecutando = True
    jugando = True 
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
                sys.exit()
        teclas = pygame.key.get_pressed()
        if teclas[K_a]:
            background_image = util.cargar_imagen('imagenes/Dragon/fondo.gif')        
            posX=100
            posY=100
            heroe = Dragon()
            heroe.defPositions(posX,posY)
            while ejecutando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ejecutando = False
                        sys.exit()
                screen.blit(background_image, (0,0))
                if jugando:
                    heroe.actualizar(sprite)
                    heroe.draw(screen)
                pygame.display.update() 
        if teclas[K_s]:
            background_image = util.cargar_imagen('imagenes/Mario/fondo.jpg')        
            posX=200
            posY=200
            adaptado = Adaptador()
            adaptado.defPositions(posX,posY) 
            while ejecutando:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        ejecutando = False
                        sys.exit()
                screen.blit(background_image, (0,0))
                if jugando:
                    adaptado.update(sprite)
                    adaptado.draw(screen)
                pygame.display.update() 

if __name__ == '__main__':
    game()

