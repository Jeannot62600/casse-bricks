import pygame
from pygame.locals import *
from math import sin, cos, pi
from brique import brique
from forme import forme


class balle(forme):
    """docstring for mur."""
    def __init__(self, coordonnees, rayon = 5, angle = 0, couleur = (255,255,255)):
        super(balle, self).__init__(coordonnees)
        self.coord = coordonnees
        self.rayon = rayon
        self.angle = angle
        self.couleur = couleur
        self.vit_set = False
        self.vitesse = 0

    def set_pos(self, x, y):
        self.coord = [x,y]

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

    def rebond(self, briq):
        x, y = self.coord
        r = 1.4*self.rayon
        if briq.appartient(x+r,y) or briq.appartient(x-r,y):
            self.angle = pi -(self.angle)
            briq.touch()
        if briq.appartient(x,y+r) or briq.appartient(x,y-r):
            self.angle = - self.angle
            briq.touch()

    def lancer(self, vitesse):
        if not self.vit_set:
            self.vitesse = vitesse
            self.vit_set = True

    def deb_set_pos(self,x, y):
        if not self.vit_set:
            self.set_pos(x,y)
