class Viagem:
    def __init__(self):
        self.__destino = ""
        self.__distancia = 0.0
        self.__litros = 0.0
        self.__consumo = 0.0  # inicializar

    def set_distancia(self, d):
        if d > 0:
            self.__distancia = d
    
    def set_destino(self, dest):
        if dest.strip() != "":
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

    def Consumo(self, a, b, c):
        self.set_destino(a)
        self.set_distancia(b)
        self.set_litros(c)
        self.__consumo = (self.__distancia / self.__litros)
        print(f"Consumo: {self.__consumo:.2f} km/l")

    def ToStr(self):
        print(f"Destino: {self.__destino}, Distância: {self.__distancia} km, Combustível: {self.__litros} litros, Consumo: {self.__consumo:.2f} km/l")


class Interface:
    @staticmethod
    def Main():
        x = Viagem()
        try:
            entrada = input("Digite o local do destino, a distância em km e a quantidade de litros de combustível:\n").split()
            a = entrada[0]
            b = float(entrada[1])
            c = float(entrada[2])
            x.Consumo(a, b, c)
            print("=" * 80)
            x.ToStr()
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")
        Interface.Menu()

    @staticmethod
    def Menu():
        response = input("1 – Calcular nova viagem, 2 – Fim\n")
        if response == "1":
            Interface.Main()
        else:
            print("Fim das viagens.")


class Pais:
    def __init__(self):
        self.__nome = ""
        self.__populacao = 0.0
        self.__area = 0.0
        self.__densidade = 0.0  # inicializar

    def set_populacao(self, d):
        if d > 0:
            self.__populacao = d
    
    def set_nome(self, n):
        if n.strip() != "":
            self.__nome = n

    def set_area(self, l):
        if l > 0:
            self.__area = l

    def get_populacao(self):        
        return self.__populacao

    def get_area(self):
        return self.__area

    def get_nome(self):
        return self.__nome

    def Densidade(self, a, b, c):
        self.set_nome(a)
        self.set_populacao(b)
        self.set_area(c)
        self.__densidade = (self.__populacao / self.__area)
        print(f"Densidade: {self.__densidade:.2f} hab/km²")

    def ToStr(self):
        print(f"PAÍS: {self.__nome}, POPULAÇÃO: {self.__populacao}, ÁREA: {self.__area} km², DENSIDADE: {self.__densidade:.2f} hab/km²")


class Interface2:
    @staticmethod
    def Calculo():
        pais = Pais()
        try:
            entrada = input("Digite o nome do país, a população e a área do país em km²:\n").split()
            a = entrada[0]
            b = float(entrada[1])
            c = float(entrada[2])
            pais.Densidade(a, b, c)
            print("=" * 80)
            pais.ToStr()
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")
        Interface2.Menu()

    @staticmethod
    def Menu():
        response = input("1 – Calcular novo país, 2 – Fim\n")
        if response == "1":
            Interface2.Calculo()
        else:
            print("Fim dos países.")


if __name__ == "__main__":
    UI = Interface
    UI.Menu()

    print("\nPAÍSES\n" + "+" * 40)
    
    UI2 = Interface2
    UI2.Menu()
