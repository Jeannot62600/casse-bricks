import pygame
from pygame.locals import *
from brique import brique
from mur import mur
from balle import balle
from math import sin, cos, pi

Clock = pygame.time.Clock()

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
continuer = 1

m1 = mur(5,12)
b1 = balle((50,50), angle = pi/6, rayon = 10, vitesse=9)


while continuer:
    fenetre.fill((0,0,0))
    for event in pygame.event.get():
    	if event.type == QUIT:
            continuer = 0
    m1.affiche(fenetre)
    b1.affiche(fenetre)
    pygame.display.flip()

    Clock.tick(30) # nb de fps
    pass
