running = True
while running:
    exercicio = int(input("exercicio: "))
    if exercicio == 1:
        # Exercicio 1
        nome = input("Digite seu nome: ")
        matricula = int(input("Digite sua matrícula: "))
        print(f"Olá, {nome}!")
        print(f"Sua matrícula é: {matricula}")
    elif exercicio == 2:
        # Exercicio 2
        print("Digite seu nome: ")
        nome = input()
        print(f"Bem-vindo(a) ao Codespace, {nome}!")
    else:
        print("digite corretamente o número do exercício")
        print("1-Exercicio 1")
        print("2-Exercicio 2")
        print("0-Para sair")
        if exercicio == 0:
            running = False
            print("Saindo...")

