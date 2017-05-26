from forme import forme
import pygame
from pygame.locals import *

class brique(forme):
    """docstring for brique."""

    def __init__(self,coordonnees, dimensions, couleur=(225,0,0), force = 1):
        super(brique, self).__init__(coordonnees)
        self.dim = dimensions
        self.coord = coordonnees
        self.force = force
        self.couleur = couleur
        self.affichage = True


    def getB(self):
        return {'coord':self.coord, 'dim':self.dim, 'col':self.couleur, 'force':self.force}

    def getBord(self):
        return self.coord + [self.coord[0]+self.dim[0], self.coord[1]+self.dim[1]]

    def affiche(self, fen):
        pygame.draw.rect(fen, self.couleur,self.coord+self.dim)

    def redim(hauteur, largeur):
        self.dim = (hauteur, largeur)

    def touch(self):
        self.force -= 1
        if self.isDead(): self.kill()

    def isDead(self):
        return self.force == 0

    def getAffiche(self):
        return self.affichage

    def appartient(self,x,y):
        a,b,c,d = self.coord[0],self.coord[1], self.coord[0]+self.dim[0], self.coord[1]+self.dim[1]
        if x > a and x < c and y > b and y < d:
            return True
        return False

    def kill(self):
        self.affichage = False
