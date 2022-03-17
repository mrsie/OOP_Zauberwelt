import random


# Oberklasse Charaktertyp
class Charaktertyp:
    anz_char = 0  # Klassen-Variable zum Zählen der Charaktere

    def __init__(self, name, leben_max, ausdauer_max):
        self.name = name
        self.gold = 0
        self.position = random.randint(0, 100)  # Positioniert den Charakter an einer zufälligen Position.
        self.leben = leben_max
        self.leben_max = leben_max
        self.ausdauer = ausdauer_max
        self.ausdauer_max = ausdauer_max
        self.kleidung = []
        self.ausruestung = []
        Charaktertyp.anz_char += 1

    def regeneration(self):
        if self.leben + 100 < self.leben_max:
            self.leben += 100
        else:
            self.leben = self.leben_max
        if self.ausdauer + 100 < self.ausdauer_max:
            self.ausdauer += 100
        else:
            self.ausdauer = self.ausdauer_max

    def laufen(self):
        pass


# Unterklasse Magier der Oberklasse Charaktertyp
class Magier(Charaktertyp):
    def __init__(self, name):  # Konstruktor der Unterklasse
        super().__init__(name, 1500, 1000)  # Konstruktor der Oberklasse
        self.magicka_max = 1500
        self.magicka = 1500
        print(name, "erscheint im Spiel an Position", self.position)

    def regeneration(self):
        super().regeneration()
        if self.magicka + 100 < self.magicka_max:
            self.magicka += 100
        else:
            self.magicka = self.magicka_max

    def heilen(self, mitspieler):
        if mitspieler.leben + 300 < self.leben_max:
            self.leben += 300
        else:
            self.leben = self.leben_max


magier1 = Magier("Gandalf")
