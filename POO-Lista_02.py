class Circulo:
    def __init__(self):
        self.__raio = 0.0

    def set_raio(self, v):
        self.__raio = v

    def get_raio(self):
        return self.__raio

    def calc_area(self):
        return 3.14 * (self.__raio ** 2)

    def calc_circunferencia(self):
        return 2 * 3.14 * self.__raio


class Viagem:
    def __init__(self):
        self.__distancia = 0.0
        self.__tempo = 0.0

    def set_distancia(self, d):
        self.__distancia = d

    def set_tempo(self, t):
        self.__tempo = t

    def get_distancia(self):
        return self.__distancia

    def get_tempo(self):
        return self.__tempo

    def velocidade_media(self):
        if self.__tempo == 0:
            return 0.0
        return self.__distancia / self.__tempo


class ContaBancaria:
    def __init__(self):
        self.__titular = ""
        self.__saldo = 0.00

    def set_titular(self, nome):
        if nome == "":
            raise ValueError("Nome inválido")
        self.__titular = nome

    def set_saldo(self, valor):
        if valor < 0:
            raise ValueError("Saldo inicial inválido")
        self.__saldo = valor

    def get_saldo(self):
        return self.__saldo

    def operacao(self):
        print(f"\nSeu nome: {self.__titular}")
        print(f"Saldo atual: R$ {self.__saldo:.2f}")
        escolha = input("Digite 'd' para depósito ou 's' para saque: ")

        if escolha == 'd':
            valor = float(input("Valor do depósito: "))
            if valor <= 0:
                print("Valor inválido.")
            else:
                self.__saldo += valor
                print("Depósito realizado com sucesso.")
        
        elif escolha == 's':
            valor = float(input("Valor do saque: "))
            if valor <= 0 or valor > self.__saldo:
                print("Saque não permitido.")
            else:
                self.__saldo -= valor
                print("Saque realizado com sucesso.")
        
        else:
            print("Operação inválida.")
        
        print(f"Saldo final: R$ {self.__saldo:.2f}")

class EntradaCinema:
    def __init__(self):
        self.__dia = ""
        self.__hora = 0

    def set_dia(self, d):
        self.__dia = d.lower()

    def set_hora(self, h):
        self.__hora = h

    def get_dia(self):
        return self.__dia

    def get_hora(self):
        return self.__hora

    def calcular_valor(self):
        dia = self.__dia
        hora = self.__hora

        if dia == "quarta":
            base = 8.0
        elif dia in ["segunda", "terca", "quinta"]:
            base = 16.0
        elif dia in ["sexta", "sabado", "domingo"]:
            base = 20.0
        else:
            raise ValueError("Dia inválido.")

        if hora >= 17 and dia != "quarta":
            base *= 1.5

        return base

    def calcular_meia(self):
        return self.calcular_valor() / 2



#   PRIMEIRA QUESTÃO
print("=== CÁLCULO DO CÍRCULO ===")
raio = float(input("Digite o raio do círculo: "))
c = Circulo()
c.set_raio(raio)
print("Raio:", c.get_raio())
print("Área:", c.calc_area())
print("Circunferência:", c.calc_circunferencia())

#   SEGUNDA QUESTÃO
print("\n=== CÁLCULO DA VIAGEM ===")
distancia = float(input("Digite a distância percorrida (km): "))
tempo = float(input("Digite o tempo da viagem (horas): "))
v = Viagem()
v.set_distancia(distancia)
v.set_tempo(tempo)
print("Distância:", v.get_distancia())
print("Tempo:", v.get_tempo())
print("Velocidade média:", v.velocidade_media(), "km/h")


#   TERCEIRA QUESTÃO
c = ContaBancaria()
c.set_titular(input("Digite o nome do titular: "))
c.set_saldo(float(input("Digite o saldo inicial: ")))
c.operacao()


#QUARTA QUESTÃO
e = EntradaCinema()
e.set_dia(input("Digite o dia da semana: "))
e.set_hora(int(input("Digite a hora (formato 24h): ")))

print("Dia:", e.get_dia())
print("Hora:", e.get_hora())
print("Valor inteiro: R$", e.calcular_valor())
print("Valor meia: R$", e.calcular_meia())
