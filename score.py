import pygame
from pygame.locals import *

class score(object):
    """docstring for score."""
    def __init__(self, value):
        self.value = value

    def gagne(self, point):
        self.value += point

    def affiche(self, fen, position, fps):
        myfont = pygame.font.SysFont("monospace", 15)
        label = myfont.render("Score :{} \n FPS :{}".format(str(self.value), str(fps)), 1, (255,255,0))
        fen.blit(label, position)
