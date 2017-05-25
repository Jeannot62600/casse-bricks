import brique

class mur(object):
    """docstring for mur."""
    def __init__(self, hauteur, largeur):
        super(mur, self).__init__()
        self.hauteur = hauteur
        self.largeur = largeur
        self.briques = []
        self.construct()
        self.lbrique = 10
        self.hbrique = 20

    def construct(self):
        for i  in range(self.hauteur):
            for j in range(self.largeur):
                self.briques.append(new brique(self.hbrique, self.lbrique))
