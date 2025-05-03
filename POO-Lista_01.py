import math

escolha = int(input("escolha uma questão para testar 1-4\n"))



class Circulo():
    def __init__(self):
        self.raio = 0

    def calcular_area(self):
        self.area = (self.raio**2)*math.pi
        print(self.area)

    def calcular_circunferencia(self):
        self.circunferecia = 2*math.pi * self.raio
        print(self.circunferecia)
if escolha == 1:
    x = Circulo()
    x.raio = int(input("raio: "))
    x.calcular_area()
    x.calcular_circunferencia()

class Viagem():
    def __init__(self):
        self.km = 0
        self.horas = 0

    def calc_velocidade(self):
        self.horas_reais = (int(self.horas.split(":")[0])) + (int(self.horas.split(":")[1])/60)
        self.velocidade = self.km / self.horas_reais
        print("velocidade =", self.velocidade, "km/h")
        

if escolha == 2:
    y = Viagem()
    y.km = int(input("km andados: "))
    y.horas = input("tempo em formato hh:mm:\n")
    y.calc_velocidade()

class Conta_Bancaria():
    def __init__(self):
        self.titular = ""
        self.id = 0
        self.saldo = 0


    def saque(self):
        self.saque_quant = int(input("quantidade para sacar: "))
        if self.saque_quant <= self.saldo:
            self.saldo -= self.saque_quant
        else:
            print("você não possui esse valor")

    def deposito(self):
        self.saldo += int(input("quantidade para depositar: "))

if escolha == 3:
    z = Conta_Bancaria()
    z.titular =  "João Pedro"
    z.id = 4345678209
    z.saldo = 50
    z.saque()
    print("saldo:", z.saldo)
    z.deposito()
    print("saldo", z.saldo)


if escolha == 4:
    class EntradaCinema():
        def __init__(self):
            self.dia = 0
            self.dia_semana = ""
            self.hora = 0
            self.preco = 0
            self.entrada = ""

        def calc_entrada(self):
            self.dia = int(input("digite o dia do mês:\n"))
            if self.dia > 31:
                print("erro")
            else:
                self.dia_semana = int(input("escreva número do dia da semana:\n1- domingo\n2- segunda-feira\n3- terça-feira\n4- quarta-feira\n5- quinta-feira\n6- sexta-feira\n7- sábado\n"))
                if self.dia_semana == 1:
                    self.dia_semana = "domingo"
                elif self.dia_semana == 2:
                    self.dia_semana = "segunda-feira"
                elif self.dia_semana == 3:
                    self.dia_semana = "terça-feira"
                elif self.dia_semana == 4:
                    self.dia_semana = "quarta-feira"
                elif self.dia_semana == 5:
                    self.dia_semana = "quinta-feira"
                elif self.dia_semana == 6:
                    self.dia_semana = "sexta-feira"
                elif self.dia_semana == 7:
                    self.dia_semana = "sábado"
                self.hora = int(input("escreva o horário em formato hh:mm\n").split(":")[0])
                if self.hora > 23:
                    print("erro no horário")
                self.entrada = input("sua entrada é uma meia-entrada? s/n\n")
                if self.entrada ==  "s":
                    self.entrada = "meia"
                elif self.entrada == "n":
                    self.entrada = "normal"
                else:
                    print("erro")

                if self.dia_semana == "segunda-feira" or self.dia_semana == "terça-feira" or self.dia_semana == "quinta-feira":
                    self.preco = 16.00
                    if self.hora >= 17 and self.hora < 0:
                        self.preco *= 1.5
                    if self.entrada == "meia":
                        self.preco *= 0.5

                elif self.dia_semana == "sexta-feira" or self.dia_semana == "sábado" or self.dia_semana == "domingo":
                    self.preco == 20.00
                    if self.hora >= 17 and self.hora < 0:
                        self.preco *= 1.5
                    if self.entrada == "meia":
                        self.preco *= 0.5

                elif self.dia_semana == "quarta-feira":
                    self.preco = 8.00

            print(f"o valor da entrada é {self.preco}R$")
    o = EntradaCinema()
    o.calc_entrada()
