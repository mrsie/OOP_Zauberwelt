class Kleidung:
  def __init__(self, bezeichnung, gewicht = 20):
    self.bezeichnung = bezeichnung
    self.gewicht = gewicht

class Umhang(Kleidung):
  anz_umhaenge = 0
  def __init__(self, bezeichnung = ""):
    Umhang.anz_umhaenge += 1
    if bezeichnung == "":
      bezeichnung = "robe_"+str(Umhang.anz_umhaenge)
    
    super().__init__(bezeichnung)
    print(bezeichnung, "wurde angefertigt.")

mein_umhang = Umhang("Tarnumhang")

class Ausruestung:
  def __init__(self, bezeichnung, gewicht = 50):
    self.bezeichnung = bezeichnung
    self.gewicht = gewicht

class Schwert(Ausruestung):
  def __init__(self, bezeichnung, angriffskraft = 20):
    super().__init__(bezeichnung)
    self.angriffskraft = angriffskraft
    print(bezeichnung, "wurde geschmiedet.")

mein_schwert = Schwert("Excalibur", angriffskraft = 50)   

class Charaktertyp:
  anz_char = 0
  def __init__(self, name):
    self.name = name
    self.gold = 0
    Charaktertyp.anz_char += 1

class Magier(Charaktertyp):
  def __init__(self, name):
    super().__init__(name)
    self.leben = 1500
    self.leben_max = 1500
    self.magicka_max = 2000
    self.magicka = 1500
    self.ausdauer = 1000
    self.ausdauer_max = 1000
    self.kleidung = []
    self.ausruestung = []


magier1 = Magier("Gandalf")


