import datetime
import math

print("escolha o exercício: 1, 2, 3, 4... 15:")
escolha = int(input())

# primeira questão
if escolha == 1:
    a = int(input())
    b = int(input())

    if a > b:
        print(a)
    elif b > a:
        print(b)
    else: print ("enguais")

# segunda questão
if escolha == 2:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    mm = [a,b,c,d]

    md = (a + b + c + d) / 4
    print("media =", md)
    print("números menores que a média")
    for i in mm:
        if i < md:
            print(i)
    print("Números maiores ou iguais à média")
    for i in mm:
        if i >= md:
            print(i)

# terceira questão
if escolha == 3:
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    numeros =  [a, b, c, d]
    
    sdp = 0
    sdi = 0
    
    for i in numeros:
        if i % 2 == 0:
            sdp += i
        else:
            sdi += i

    print("soma dos pares", sdp)
    print("soma dos ímpares", sdi)

# quarta questão
if escolha == 4:
    a = input("Digite o primeiro horário no formato hh:mm\n")
    hora = datetime.datetime.strptime(a, "%H:%M")
    b = input("Digite o segundo horário no formato hh:mm\n")
    hora2 = datetime.datetime.strptime(b, "%H:%M")


    soma = hora + (hora2 - datetime.datetime(1900, 1, 1))
    resultado = soma.time()
    print(resultado.strftime("%H:%M"))

# quinta questão
if escolha ==  5:
    a = int(input("informe o número do mês\n"))

    meses = {1 : "janeiro", 2 : "fevereiro", 3 : "março", 4 : "abril" , 5 :  "maio",  6 : "junho", 7 : "julho" , 8 : "agosto", 9 : "setembro", 10 : "outrubro", 11 : "novembro", 12 : "dezembro"}
  
    if a < 4:
        print("O mês de", meses[a] ,"é do primeiro trimestre do ano")
    if a > 3 and a < 7:
        print("O mês de", meses[a] ,"é do segundo trimestre do ano")
  
    if a > 6 and a < 10:
        print("O mês de", meses[a] ,"é do terceiro trimestre do ano")
    if a > 9:
        print("O mês de", meses[a] ,"é do quarto trimestre do ano")

# sexta questão
if escolha == 6:
    a = int(input("Digite três valores inteiros\n"))
    b = int(input())
    c = int(input())
    menor = min([a,b,c])
    maior = max([a,b,c])
    print("A soma do maior com o menor número é", maior + menor)

# sétima questão
if escolha == 7:
    a = float(input("Digite o coeficiente a: "))
    b = float(input("Digite o coeficiente b: "))
    c = float(input("Digite o coeficiente c: "))

    if a == 0:
        if b != 0:
            x = -c / b
            print(f"Equação de 1º grau. Raiz: {x}")
        else:
            print("Erro" if c != 0 else "Equação indeterminada.")
    else:
        delta = b**2 - 4*a*c

        if delta < 0:
            print("impossível calcular")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"As raízes são: {x1} e {x2}")

# oitava questão
if escolha == 8:
    a = int(input("Digite três valores inteiros\n"))
    b = int(input())
    c = int(input())
    d = int(input())
    
    if a == b or b == c or c == d or b == d or  a == d or a == c:
        print("erro")
    else:
        menor = min([a,b,c, d])
        maior = max([a,b,c, d])
        print("Maior valor =",maior)
        print("Menor valor =",menor)
        print("A soma do maior com o menor número é", maior + menor)

# nona questão
if escolha == 9:
    hora = input("Digite o horário no formato hh:mm\n")

    try:
        partes = hora.split(":")
        if len(partes) != 2:
            raise ValueError
        h = int(partes[0])
        m = int(partes[1])
    except ValueError:
        print("Hora Inválida")
        exit()

    if h < 0 or h > 23 or m < 0 or m > 59:
        print("Hora Inválida")
        exit()

    h = h % 12

    angulo_hora = h * 30 + m * 0.5
    angulo_minuto = m * 6

    diferenca = abs(angulo_hora - angulo_minuto)
    menor_angulo = diferenca if diferenca <= 180 else 360 - diferenca

    if menor_angulo.is_integer():
        menor_angulo = int(menor_angulo)

    print(f"Menor ângulo entre os ponteiros = {menor_angulo} graus")

if escolha==10:
    d = input("Digite uma data no formato dd/mm/aaaa\n").split("/")
    dia = int(d[0])
    mes = int(d[1])
    ano = int(d[2])

    if mes < 0 or mes > 12:
        print("A data informada não é válida")
    if dia > 31 or dia < 0:
        print("A data informada não é válida")
    if mes == 2 and dia >29:
        print("A data informada não é válida")
    if mes % 2 == 0 and dia > 31:
        print("A data informada não é válida")
    if mes % 2 != 0 and dia > 30:
        print("A data informada não é válida")
    if ano < 1900 or ano > 2100:
        print("A data informada não é válida") 
