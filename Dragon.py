import pygame
from pygame.sprite import Sprite
from pygame import *
import util


class Dragon(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        self.velocidad = 1

    def Posic(self, auxPosX, auxPosY):
        self.posX = auxPosX
        self.posY = auxPosY
        
    def set_sprites(self, sprite):
        self.imagenes = sprite

    def Dere(self):
        self.image = util.cargar_imagen('imagenes/Dragon/d1.png')
        self.posX += self.velocidad
                
    def Izq(self):
        self.image = util.cargar_imagen('imagenes/Dragon/i1.png')
        self.posX -= self.velocidad      
    
    def actualizar(self,sprite):
        self.image= util.cargar_imagen('imagenes/Dragon/i1.png')      
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            self.Izq()
        if teclas[K_RIGHT]:
            self.Dere()
        
    def draw(self, screen):
        screen.blit(self.image, (self.posX,self.posY))