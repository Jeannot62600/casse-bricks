from forme import forme
import pygame
from pygame.locals import *

class brique(forme):
    """docstring for brique."""

    def __init__(self,coordonnees, dimensions, couleur, force = 1):
        super(brique, self).__init__(coordonnees)
        self.dim = dimensions
        self.coord = coordonnees
        self.force = force
        self.couleur = couleur


    def getB(self):
        return {'coord':self.coord, 'dim':self.dim, 'col':self.couleur, 'force':self.force}

    def affiche(self, fen):
        pygame.draw.rect(fen, self.couleur,self.coord+self.dim)


    def redim(hauteur, largeur):
        self.dim = (hauteur, largeur)

    def touch():
        self.force -= 1
        if self.isDead(): self.kill() 

    def isDead():
        return self.force == 0

    def kill():
        self.affiche = False
