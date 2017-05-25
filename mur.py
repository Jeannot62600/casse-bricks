from brique import brique
from random import randint

class mur(object):
    """docstring for mur."""
    def __init__(self, hauteur, largeur):
        super(mur, self).__init__()
        self.hauteur = hauteur
        self.largeur = largeur
        self.briques = []
        self.lbrique = 50
        self.hbrique = 30
        self.construct()


    def construct(self):
        for i  in range(self.hauteur):
            for j in range(self.largeur):
                self.briques.append(brique((j*(self.lbrique+5), i*(self.hbrique+5)),(self.lbrique, self.hbrique),[randint(0,255) for k in range(3)]))

    def affiche(self,fen):
        for br in self.briques:
            br.affiche(fen)
