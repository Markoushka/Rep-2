class Figura:

    def __init__(self, color, chislo_p, coordinaty):
        self.color = color
        self.chislo_p = chislo_p
        self.coordinaty = coordinaty

    def ShowInfo(self):
        print("Color: ", self.color, "chislo_p: ", self.chislo_p, "Coordinaty:", self.coordinaty)

class Pryamougolnik(Figura):
    def __init__(self, color, chislo_p, coordinaty):
        super().__init__(color, chislo_p, coordinaty)

myPryamougolnik = Pryamougolnik("Seroburomalinoviy", 3.14, 358.256)
myPryamougolnik.ShowInfo()
