import math

print("escolha o exercício: 1, 2 ou 3:")
escolha = int(input())

if escolha == 1:
    print("Digite seu nome completo:")

    nome = str(input())

    primeiro_nome = nome.split()[0]
    print("Bem-vindo(a) ao Python,",primeiro_nome)

if escolha == 2:
    print("Digite a nota do primeiro bimestre da disciplina:")
    primiro_bimestre = int(input())*2
    print("Digite a nota do segundo bimestre da disciplina:")
    segundo_bimestre = int(input())*3
    media_parcial = ((primiro_bimestre+segundo_bimestre)/5)
    print("Média parcial =", media_parcial)

if escolha == 3:
    print("Digite a base e a altura do retângulo")
    base = int(input())
    altura = int(input())
    area = base*altura
    perimetro = (altura*2) + (base*2)
    diagonal = math.sqrt((altura**2)+(base**2))
    print(f"Área = {area} - Perímetro = {perimetro} - Diagonal = {diagonal}")

if escolha == 4:
    print("Digite uma frase:")
    frase = input()
    print(frase[ frase.rindex(" ") + 1: ])
