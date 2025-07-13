import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.set_nome(nome)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.set_nascimento(nascimento)

    def set_nome(self, nome):
        if isinstance(nome, str) and nome.strip():
            self.__nome = nome
        else:
            raise ValueError("Nome inválido. Não há um texto.")

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and cpf.isdigit() and len(cpf) == 11:
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido. Deve ter 11 dígitos numéricos.")
        
    def set_telefone(self, telefone):
        if isinstance(telefone, str) and telefone.isdigit() and len(telefone) >= 10:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido. Deve ter pelo menos 10 dígitos numéricos.")

    def set_nascimento(self, nascimento):
        if isinstance(nascimento, str) and nascimento:
            try:
                self.__nascimento = datetime.datetime.strptime(nascimento, "%d/%m/%Y")
            except ValueError:
                raise ValueError("Data de nascimento inválida. Use o formato DD/MM/YYYY.")
        
    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_telefone(self):
        return self.__telefone
        
    def get_nascimento(self):
        return self.__nascimento
    
    def idade(self):
        hoje = datetime.date.today()
        nascimento = self.__nascimento.date()
        anos = hoje.year - nascimento.year
        meses = hoje.month - nascimento.month
        if hoje.day < nascimento.day:
            meses -= 1
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses"
    
    def __str__(self):
        nasc_formatada = self.__nascimento.strftime("%d/%m/%Y")
        return (f"Paciente:\n"
                f"Nome: {self.__nome}\n"
                f"CPF: {self.__cpf}\n"
                f"Telefone: {self.__telefone}\n"
                f"Nascimento: {nasc_formatada}\n"
                f"Idade: {self.idade()}")


class PacienteUI:
    def __init__(self):
        self.__pacientes = []

    def menu(self):
        while True:
            print("\n=== MENU PACIENTE ===")
            print("1. Cadastrar novo paciente")
            print("2. Listar pacientes")
            print("3. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__cadastrar()
            elif opcao == "2":
                self.__listar()
            elif opcao == "3":
                print("Encerrando sistema de pacientes...")
                break
            else:
                print("Opção inválida!")

    def __cadastrar(self):
        print("\n=== Cadastro de Paciente ===")
        nome = input("Nome: ")
        cpf = input("CPF (somente números): ")
        telefone = input("Telefone (somente números): ")
        nascimento = input("Data de nascimento (DD/MM/YYYY): ")

        try:
            paciente = Paciente(nome, cpf, telefone, nascimento)
            self.__pacientes.append(paciente)
            print("\n--- Paciente cadastrado com sucesso ---")
            print(paciente)
        except ValueError as e:
            print(f"Erro ao criar paciente: {e}")

    def __listar(self):
        if not self.__pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            print("\n--- Lista de Pacientes ---")
            for p in self.__pacientes:
                print("-" * 30)
                print(p)

    @staticmethod
    def executar():
        PacienteUI.main()

    @staticmethod
    def main():
        app = PacienteUI()
        app.menu()


if __name__ == "__main__":
    PacienteUI.executar()
