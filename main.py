import pygame
from pygame.locals import *
from brique import brique
from mur import mur
from balle import balle
from math import sin, cos, pi
from raquette import raquette
from score import score

Clock = pygame.time.Clock()
fps = 30

pygame.init()
fenetre = pygame.display.set_mode((640, 480), RESIZABLE)
pygame.mouse.set_visible ( False )
continuer = 1

m1 = mur(5,12)
b1 = balle((500,300), angle = pi/6, rayon = 10)
r1 = raquette([200,430], [100,10])
s1 = score(0)


while continuer:
    fenetre.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        if event.type == MOUSEMOTION:
            r1.deplace(event.pos[0]-50)
            b1.deb_set_pos(event.pos[0], 410)
        if event.type == KEYDOWN and event.key == K_SPACE:
            b1.lancer(vitesse=300/fps)

    r1.collision(b1)
    m1.collision(b1, s1)
    m1.affiche(fenetre)
    b1.affiche(fenetre)
    r1.affiche(fenetre)
    s1.affiche(fenetre, (0,0), fps)
    pygame.display.flip()

    Clock.tick(fps) # nb de fps
    pass
