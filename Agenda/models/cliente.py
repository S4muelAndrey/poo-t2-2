# models/cliente.py
import json

class Cliente:
    def __init__(self, id, nome, email, fone, senha):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)

    # getters
    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
    def get_email(self): return self.__email
    def get_fone(self): return self.__fone
    def get_senha(self): return self.__senha

    # setters (validação leve; lançam ValueError quando inválido)
    def set_id(self, id):
        # permite 0, números e strings não vazias; bloqueia None ou string vazia
        if id is None:
            raise ValueError("ID não pode ser None")
        if isinstance(id, str) and id == "":
            raise ValueError("ID não pode ser vazio")
        self.__id = id

    def set_nome(self, nome):
        if nome is None or (isinstance(nome, str) and nome.strip() == ""):
            raise ValueError("Nome não pode ser vazio")
        self.__nome = nome

    def set_email(self, email):
        if email is None or (isinstance(email, str) and email.strip() == ""):
            raise ValueError("E-mail não pode ser vazio")
        self.__email = email

    def set_fone(self, fone):
        if fone is None or (isinstance(fone, str) and fone.strip() == ""):
            raise ValueError("Fone não pode ser vazio")
        self.__fone = fone

    def set_senha(self, senha):
        if senha is None or (isinstance(senha, str) and senha.strip() == ""):
            raise ValueError("Senha não pode ser vazia")
        self.__senha = senha

    # serialização / desserialização (nomes compatíveis com seu código original)
    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome,
            "email": self.__email,
            "fone": self.__fone,
            "senha": self.__senha
        }

    @staticmethod
    def from_json(dic):
        return Cliente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"])

    def __str__(self):
        return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone} - {self.__senha}"


class ClienteDAO:
    __objetos = []
    arquivo = "clientes.json"

    @classmethod
    def abrir(cls):
        cls.__objetos = []
        try:
            with open(cls.arquivo, mode="r", encoding="utf-8") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Cliente.from_json(dic)
                    cls.__objetos.append(obj)
        except FileNotFoundError:
            # arquivo não existe ainda: retorna lista vazia
            cls.__objetos = []
        except json.JSONDecodeError:
            # arquivo inválido/corrompido: ignora e retorna lista vazia
            cls.__objetos = []

    @classmethod
    def salvar(cls):
        # sempre escreve explicitamente uma lista de dicts
        with open(cls.arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in cls.__objetos], arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        # calcula novo id (maior existente + 1)
        id_max = 0
        for aux in cls.__objetos:
            try:
                if aux.get_id() > id_max:
                    id_max = aux.get_id()
            except Exception:
                pass
        # atualiza id interno mesmo que set_id valide — usar atributo privado evita validação ambígua
        obj._Cliente__id = id_max + 1
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.__objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        for i, aux in enumerate(cls.__objetos):
            if aux.get_id() == obj.get_id():
                cls.__objetos[i] = obj
                cls.salvar()
                return
        # se não encontrou, adiciona
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.__objetos = [aux for aux in cls.__objetos if aux.get_id() != obj.get_id()]
        cls.salvar()
