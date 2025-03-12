import math
class Circulo:
    def __init__(self, r):
        self.radio = r
    def getArea(self):
        return math.pi * self.radio ** 2
    def getPerimetro(self):
        return 2 * math.pi * self.radio
    
c1 = Circulo(1)
print("Area = ", c1.getArea())
print("Perimetro = ", c1.getPerimetro())

c2 = Circulo(2)
print("Area = ", c2.getArea())
print("Perimetro = ", c2.getPerimetro())
 
 
