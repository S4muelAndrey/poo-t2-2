import datetime

class Contato:
    def __init__(self, id, nome, email, fone, nascimento):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone
        if isinstance(nascimento, str):
            self.__nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
        else:
            self.__nascimento = nascimento

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def set_fone(self, fone):
        self.__fone = fone

    def set_nascimento(self, nascimento):
        if isinstance(nascimento, str):
            self.__nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
        else:
            self.__nascimento = nascimento

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def get_nascimento(self):
        return self.__nascimento

    def __str__(self):
        return (f"ID: {self.__id}\n"
                f"Nome: {self.__nome}\n"
                f"E-mail: {self.__email}\n"
                f"Telefone: {self.__fone}\n"
                f"Nascimento: {self.__nascimento.strftime('%d/%m/%Y')}")
class ContatoUI:
    def __init__(self):
        self.__contatos = []

    def menu(self):
        while True:
            print("\n--- MENU PRINCIPAL ---")
            print("1. Inserir novo contato")
            print("2. Listar todos os contatos")
            print("3. Atualizar um contato")
            print("4. Excluir um contato")
            print("5. Pesquisar por nome")
            print("6. Ver aniversariantes do mês")
            print("7. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.inserir()
            elif opcao == "2":
                self.listar()
            elif opcao == "3":
                self.atualizar()
            elif opcao == "4":
                self.excluir()
            elif opcao == "5":
                self.pesquisar()
            elif opcao == "6":
                self.aniversariantes()
            elif opcao == "7":
                print("Encerrando agenda...")
                break
            else:
                print("Opção inválida!")

    def inserir(self):
        try:
            id = int(input("ID: "))
            nome = input("Nome: ")
            email = input("Email: ")
            fone = input("Telefone: ")
            nascimento = input("Data de nascimento (DD/MM/YYYY): ")
            novo = Contato(id, nome, email, fone, nascimento)
            self.__contatos.append(novo)
            print("Contato inserido com sucesso!")
        except Exception as e:
            print(f"Erro: {e}")

    def listar(self):
        if not self.__contatos:
            print("Nenhum contato cadastrado.")
        else:
            for contato in self.__contatos:
                print("-" * 30)
                print(contato)

    def atualizar(self):
        id = int(input("Informe o ID do contato a ser atualizado: "))
        for c in self.__contatos:
            if c.get_id() == id:
                nome = input("Novo nome: ")
                email = input("Novo email: ")
                fone = input("Novo telefone: ")
                nascimento = input("Nova data de nascimento (DD/MM/YYYY): ")
                c.set_nome(nome)
                c.set_email(email)
                c.set_fone(fone)
                c.set_nascimento(nascimento)
                print("Contato atualizado com sucesso.")
                return
        print("Contato não encontrado.")

    def excluir(self):
        id = int(input("Informe o ID do contato a ser excluído: "))
        for c in self.__contatos:
            if c.get_id() == id:
                self.__contatos.remove(c)
                print("Contato removido com sucesso.")
                return
        print("Contato não encontrado.")

    def pesquisar(self):
        termo = input("Digite parte do nome a pesquisar: ").lower()
        encontrados = [c for c in self.__contatos if termo in c.get_nome().lower()]
        if encontrados:
            for c in encontrados:
                print("-" * 30)
                print(c)
        else:
            print("Nenhum contato encontrado.")

    def aniversariantes(self):
        mes_atual = datetime.date.today().month
        aniversariantes = [c for c in self.__contatos if c.get_nascimento().month == mes_atual]
        if aniversariantes:
            print(f"\nContatos que fazem aniversário em {mes_atual}:")
            for c in aniversariantes:
                print("-" * 30)
                print(c)
        else:
            print("Nenhum aniversariante neste mês.")

    @staticmethod
    def executar():
        ContatoUI.main()

    @staticmethod
    def main():
        app = ContatoUI()
        app.menu()

ContatoUI.executar()
