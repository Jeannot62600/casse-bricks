from brique import brique
from random import randint
from balle import balle

class mur(object):
    """docstring for mur."""
    def __init__(self, hauteur, largeur):
        super(mur, self).__init__()
        self.hauteur = hauteur
        self.largeur = largeur
        self.briques = []
        self.lbrique = 50
        self.hbrique = 30
        self.palette = [(1,(255,0,0)), (2,(0,255,0)), (3,(0,0,255))]
        self.construct()

    def construct(self):
        for i  in range(self.hauteur):
            for j in range(self.largeur):
                choix = self.palette[randint(0,2)]
                self.briques.append(brique((j*(self.lbrique+5),50+ i*(self.hbrique+5)),(self.lbrique, self.hbrique),choix[1], force= choix[0]))

    def affiche(self,fen):
        for br in self.briques:
            if (br.getAffiche()): br.affiche(fen)

    def collision(self, bal, s1):
        for br in self.briques:
            bal.rebond(br)
            if br.isDead():
                self.briques.pop(self.briques.index(br))
            s1.gagne(10)
            br.maj_color(self.palette)
