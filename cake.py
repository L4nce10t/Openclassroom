"""class Cake:
    def __init__(self, flavor):
        self.flavor = flavor

    def coup_part(self):
        print("On coupe le gateau en 3")


cake_choc = Cake("chocolat")
print(cake_choc.flavor)
cake_choc.coup_part()"""


class Bird:
    """Un oiseau. 🐦"""

    # ici on utilise deux attributs de classe.
    names = ("mouette", "pigeon", "moineau", "hirrondelle")
    positions = {}

    def __init__(self, name):
        """Les attributs définis ici sont des attributs d'instance."""
        self.position = 1, 2
        self.name = name

        # On accède à l'attribut de classe "positions" avec self (c'est possible).
        self.positions[self.position] = self.name

    # On precise
    @classmethod
    def find_bird(cls, position):
        """Retrouve un oiseau selon la position donnée."""
        if position in cls.positions:
            return f"On a trouvé un {cls.positions[position]} !"

        return "On a rien trouvé..."


# On peut accéder aux variables de classe sans instanciation.
print(Bird.find_bird((2, 5)))

# On instancie un oiseau
bird = Bird("mouette")

# On le retrouve avec la méthode find_bird.
print(bird.find_bird((1, 2)))
