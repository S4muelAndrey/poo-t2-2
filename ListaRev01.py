import datetime

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

if escolha == 4:
    a = input("Digite o primeiro horário no formato hh:mm\n")
    hora = datetime.datetime.strptime(a, "%H:%M")
    b = input("Digite o segundo horário no formato hh:mm\n")
    hora2 = datetime.datetime.strptime(b, "%H:%M")


    soma = hora + (hora2 - datetime.datetime(1900, 1, 1))
    resultado = soma.time()
    print(resultado.strftime("%H:%M"))

if escolha ==  5:
    a = int(input())

    meses = {1 : "janeiro", 2 : "fevereiro", 3 : "março", 4 : "abril" , 5 :  "maio",  6 : "junho", "julho" : 7 , 8 : "agosto", 9 : "setembro", 10 : "outrubro", 11 : "novembro", 12 : "dezembro"}
  
    print(meses[a])
