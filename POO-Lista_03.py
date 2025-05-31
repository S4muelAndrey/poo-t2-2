import math

class Retangulo:
    def __init__(self, b, h):
        if b <= 0 or h <= 0:
            raise ValueError("Base e altura devem ser positivas.")
        self.__b = b
        self.__h = h

    def SetBase(self, b):
        if b <= 0:
            raise ValueError("Base deve ser positiva.")
        self.__b = b

    def SetAltura(self, h):
        if h <= 0:
            raise ValueError("Altura deve ser positiva.")
        self.__h = h

    def GetBase(self):
        return self.__b

    def GetAltura(self):
        return self.__h

    def CalcArea(self):
        return self.__b * self.__h

    def CalcDiagonal(self):
        return math.sqrt(self.__b ** 2 + self.__h ** 2)

    def ToString(self):
        return f"Retângulo: base={self.__b}, altura={self.__h}, área={self.CalcArea():.2f}, diagonal={self.CalcDiagonal():.2f}"

class interface1:
    def executar(self):
        try:
            b = float(input("Informe a base do retângulo: "))
            h = float(input("Informe a altura do retângulo: "))
            r = Retangulo(b, h)
            print(r.ToString())
        except ValueError as e:
            print("Erro:", e)

class Frete:
    def __init__(self, distancia, peso):
        if distancia <= 0 or peso <= 0:
            raise ValueError("Distância e peso devem ser positivos.")
        self.__distancia = distancia
        self.__peso = peso

    def SetDistancia(self, d):
        if d <= 0:
            raise ValueError("Distância deve ser positiva.")
        self.__distancia = d

    def SetPeso(self, p):
        if p <= 0:
            raise ValueError("Peso deve ser positivo.")
        self.__peso = p

    def GetDistancia(self):
        return self.__distancia

    def GetPeso(self):
        return self.__peso

    def CalcFrete(self):
        return self.__peso * self.__distancia * 0.01

    def ToString(self):
        return f"Frete: distância={self.__distancia}km, peso={self.__peso}kg, valor=R$ {self.CalcFrete():.2f}"

class Interface2:
    def executar(self):
        try:
            d = float(input("Informe a distância (em km): "))
            p = float(input("Informe o peso da carga (em kg): "))
            f = Frete(d, p)
            print(f.ToString())
        except ValueError as e:
            print("Erro:", e)

import math

class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def setA(self, a): self.__a = a
    def setB(self, b): self.__b = b
    def setC(self, c): self.__c = c

    def getA(self): return self.__a
    def getB(self): return self.__b
    def getC(self): return self.__c

    def Delta(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def TemRaizesReais(self):
        return self.Delta() >= 0

    def Raiz1(self):
        if not self.TemRaizesReais():
            return None
        return (-self.__b + math.sqrt(self.Delta())) / (2 * self.__a)

    def Raiz2(self):
        if not self.TemRaizesReais():
            return None
        return (-self.__b - math.sqrt(self.Delta())) / (2 * self.__a)

    def ToString(self):
        return f"f(x) = {self.__a}x² + {self.__b}x + {self.__c}"

class UIEquacaoSegundoGrau:
    def executar(self):
        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))

            eq = EquacaoSegundoGrau(a, b, c)
            print(eq.ToString())
            print("Delta:", eq.Delta())

            if eq.TemRaizesReais():
                print("Raiz 1:", eq.Raiz1())
                print("Raiz 2:", eq.Raiz2())
            else:
                print("A equação não possui raízes reais.")
        except Exception as e:
            print("Erro:", e)


#   ---------------------------------------
#   |       EquacaoSegundoGrau            |
#   ---------------------------------------
#   | - __a: double                       |
#   | - __b: double                       |
#   | - __c: double                       |
#   ---------------------------------------
#   | + setA(a: double): void             |
#   | + setB(b: double): void             |
#   | + setC(c: double): void             |
#   | + getA(): double                    |
#   | + getB(): double                    |
#   | + getC(): double                    |
#   | + Delta(): double                   |
#   | + TemRaizesReais(): bool            |
#   | + Raiz1(): double or None           |
#   | + Raiz2(): double or None           |
#   | + ToString(): string                |
#   ---------------------------------------
