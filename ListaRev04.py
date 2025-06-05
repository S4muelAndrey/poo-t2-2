class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0.0
        self.__litros = 0.0

    def set_distancia(self, d):
        if d > 0:
            self.__distancia = d
    
    def set_destino(self, dest):
        if dest.split()[0] != "":
            self.__destino = dest

    def set_litros(self, l):
        if l > 0:
            self.__litros = l

    def get_distancia(self):
        
        return self.__distancia

    def get_litros(self):
        return self.__litros

    def get_destino(self):
        return self.__destino

    def velocidade_media(self):
        if self.__litros == 0:
            return 0.0
        return self.__distancia / self.__litros


    def Consumo(self, a, b, c):
        self.set_destino(a)
        self.set_distancia(b)
        self.set_litros(c)
        self.__consumo = (self.__distancia / self.__litros)
        print(self.__consumo)

    def ToStr(self):
        print(f"{(self.__destino)}, {(self.__distancia)}km, {self.__litros} litros, consumo = {self.__consumo}")
        
    
class Interface:
    @staticmethod
    def Main():
        x = Viagem()
        atributos = input("digite o local do destino, a distância em km e a quantidade de litro de combustível\n").split()
        a = atributos[0]
        b = int(atributos[1])
        c = int(atributos[2])
        x.Consumo(a, b, c)
        print("===============================================================================\n")
        x.ToStr()
        Interface.Menu()

    @staticmethod
    def Menu():
        response = input("1 – Calcular, 2 – Fim\n")
        if response == "1":
            Interface.Main()
        else:
            return("fim.")

UI = Interface
UI.Menu()
