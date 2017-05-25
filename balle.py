import pygame
from pygame.locals import *
from math import sin, cos, pi


class balle(object):
    """docstring for mur."""
    def __init__(self, coordonnees, rayon = 5, angle = 0, couleur = (255,255,255), vitesse = 3):
        self.coord = coordonnees
        self.rayon = rayon
        self.angle = angle
        self.couleur = couleur
        self.vitesse = vitesse

    def affiche(self, fen):
        self.newpos()
        pygame.draw.circle(fen, self.couleur,[int(x) for x in self.coord], self.rayon)

    def newpos(self):
        self.rebond_mur()
        self.coord = (self.coord[0] +  self.vitesse*cos(self.angle), self.coord[1] + self.vitesse*sin(self.angle))

    def rebond_mur(self):
        r = self.rayon
        if (self.coord[0]-r < 0 or self.coord[0]+r > 640):
            self.angle = pi -(self.angle)
        if (self.coord[1]-r < 0 or self.coord[1]+r > 480):
            self.angle = - self.angle
