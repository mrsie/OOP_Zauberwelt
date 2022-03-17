import random

# Oberklasse Charaktertyp
class Charaktertyp:
  anz_char = 0 # Attribut zum Zählen der Charaktere
  def __init__(self, name, leben_max = 1000, ausdauer_max = 1000):
    self.name = name
    self.gold = 0
    self.position = random.randint(0,100)
    self.leben = leben_max
    self.leben_max = leben_max
    self.ausdauer = ausdauer_max
    self.ausdauer_max = ausdauer_max
    self.kleidung = []
    self.ausrüstung = []
    Charaktertyp.anz_char += 1
    

# Unterklasse Magier der Oberklasse Charaktertyp
class Magier(Charaktertyp):
  def __init__(self, name):
    super().__init__(name, leben_max = 1500)
    self.magicka_max = 1500
    self.magicka = 1500

magier1 = Magier("Gandalf")


