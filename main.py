import pygame
from pygame.locals import *
from brique import brique
from mur import mur
from balle import balle
from math import sin, cos, pi
from raquette import raquette

Clock = pygame.time.Clock()
fps = 30

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
continuer = 1

m1 = mur(5,12)
b1 = balle((500,300), angle = pi/6, rayon = 10, vitesse=300/fps)
r1 = raquette([200,430], [50,5])


while continuer:
    fenetre.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEMOTION:
            r1.deplace(event.pos[0])
    r1.collision(b1)
    m1.collision(b1)
    m1.affiche(fenetre)
    b1.affiche(fenetre)
    r1.affiche(fenetre)
    pygame.display.flip()

    Clock.tick(fps) # nb de fps
    pass
