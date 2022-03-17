# Oberklasse Charaktertyp
class Charaktertyp:
    anz_char = 0  # Klassen-Variable zum Zählen der Charaktere

    def __init__(self, name, leben_max, ausdauer_max):
        self.name = name
        self.gold = 0
        self.leben = leben_max
        self.leben_max = leben_max
        self.ausdauer = ausdauer_max
        self.ausdauer_max = ausdauer_max
        self.kleidung = []
        self.ausruestung = []
        Charaktertyp.anz_char += 1
        print(self.name, "erscheint im Spiel.")


# Unterklasse Magier der Oberklasse Charaktertyp
class Magier(Charaktertyp):
    def __init__(self, name):  # Konstruktor der Unterklasse
        super().__init__(name, 1500, 1000)  # Konstruktor der Oberklasse
        self.magicka_max = 1500
        self.magicka = 1500

    def heilen(self):
        if self.leben + 300 < self.leben_max:
            self.leben += 300
        else:
            self.leben = self.leben_max


magier1 = Magier("Gandalf")
# magier1.leben = 1000
# magier1.heilen()
# print(magier1.leben)

# 1. Aufgabe:
# Erstelle eine Unterklasse Ritter der Oberklasse Charaktertyp
# Ein Ritter soll standardmäßig ein maximales Leben von 2000 und eine maximale Ausdauer von 1800 haben.
