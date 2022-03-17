class Magier:
  anz_char = 0
  def __init__(self, name):
    self.leben = 1500
    self.leben_max = 1500
    self.magicka_max = 1500
    self.magicka = 1500
    self.ausdauer = 1500
    self.ausdauer_max = 1500
    self.gold = 0
    self.name = name
    Magier.anz_char += 1

  def heilen(self):
    if self.leben + 300 < self.leben_max:
      self.leben += 300
    else:
      self.leben = self.leben_max

magier1 = Magier(name="Gandalf")
magier1.leben = 1000
magier1.heilen()
print(magier1.leben)
