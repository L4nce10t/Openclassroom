import random
import abc


class Film:
    def __init__(self, name):
        self.name = name

    def watch(self):
        print("je regarde un film wouhou \n")


class Ecran():
    def __init__(self, marque, taille):
        self.marque = marque
        self.taille = taille

    def affiche(self):
        print(
            f"On remercie à '{self.marque}' de nous avoir envoyé cette écran")


class Filmcassette(Film):
    def __init__(self, name):
        self.name = name
        x = random.randint(1, 2)
        if x == 2:
            self.magnetic_tap = False
        elif x == 1:
            self.magnetic_tap = True

    def rewind(self):
        print("Voyons si il faut rembobiner la cassette")
        if self.magnetic_tap == True:
            print("Pas besoin de rembobiner\n")
        else:
            print("On rembobine\n")


class FilmDVD(Film):

    def __init__(self, name):
        self.name = name

    def menu(self):
        # L'option f demande a la fonction print de regarder ce qu'il y a dans le variable {}
        # Ici on se refere au nom de l'objet même qu'on initié avec le constructeur __init__
        print(f"Voici le menu du film '{self.name}'")


film = Film("Vice-versa")
film2 = Filmcassette("La folie des grandeurs")
film3 = FilmDVD("La La La Land")

film2.rewind()
film2.watch()
film3.menu()
