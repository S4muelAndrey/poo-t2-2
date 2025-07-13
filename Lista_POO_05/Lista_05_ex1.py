import datetime

class Paciente:
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone
        self.set_nascimento(nascimento)

    def set_nome(self, nome):
        if isinstance(nome, str) and nome:
            self.__nome = nome
        else:
            raise ValueError("Nome inválido. Não há um texto.")

    def set_cpf(self, cpf):
        if isinstance(cpf, str) and len(cpf) == 11:
            self.__cpf = cpf
        else:
            raise ValueError("CPF inválido. Deve ter 11 dígitos.")
        
    def set_telefone(self, telefone):
        if isinstance(telefone, str) and len(telefone) >= 10:
            self.__telefone = telefone
        else:
            raise ValueError("Telefone inválido. Deve ter pelo menos 10 dígitos.")

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
        return f"Paciente(nome={self.__nome}, cpf={self.__cpf}, telefone={self.__telefone}, nascimento={self.__nascimento})"

# UI de teste
def pacienteUI():
    print("=== Cadastro de Paciente ===")
    nome = input("Nome: ")
    cpf = input("CPF (somente números): ")
    telefone = input("Telefone: ")
    nascimento = input("Data de nascimento (DD/MM/YYYY): ")

    try:
        paciente = Paciente(nome, cpf, telefone, nascimento)
        print("\n--- Dados do Paciente ---")
        print(paciente)
        print(f"\nIdade: {paciente.idade()}")
    except ValueError as e:
        print(f"Erro ao criar paciente: {e}")

pacienteUI()
