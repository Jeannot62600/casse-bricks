import pygame
from pygame.locals import *
from brique import brique

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
continuer = 1

b1 = brique(coordonnees = (10,20), dimensions = (20,30), couleur = (255,0,0))
print(b1.getB()['col'])
while continuer:
    for event in pygame.event.get():
    	if event.type == QUIT:
            continuer = 0
    b1.affiche(fenetre)
    pygame.display.flip()
    pass
