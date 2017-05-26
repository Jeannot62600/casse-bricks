from brique import brique
import pygame
from pygame.locals import *


class raquette(brique):
    """docstring for raquette."""
    def __init__(self,  coordonnees , dimensions):
        super(raquette, self).__init__(coordonnees, dimensions, force = 999999)
        self.dim = dimensions
        self.coord = coordonnees

    def deplace(self, xx):
        self.coord[0] = xx

    def affiche(self, fen):
        pygame.draw.rect(fen, self.couleur,self.coord+self.dim)

    def collision(self, bal):
        bal.rebond(self)
