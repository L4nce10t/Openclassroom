
class Boite_Out:

    def __init__(self):
        self.outils = []

    def ajout_out(self, outil):
        self.outils.append(outil)

    def enlev_out(self, outil):
        index = self.outils.index(outil)
        del self.outils[index]


class Marteau:

    def __init__(self, color):
        self.color = color

    def plant(self, vis):
        pass

    def devis(self, vis):
        pass

    def change_color(self, color):
        pass


class Tournevis:

    def __init__(self, taille):
        self.taille = taille
