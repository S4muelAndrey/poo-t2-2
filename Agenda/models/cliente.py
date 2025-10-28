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

    # setters usando try/except
    def set_id(self, id):
        try:
            if id is None:
                raise ValueError
            if isinstance(id, str) and id.strip() == "":
                raise ValueError
            self.__id = id
        except Exception:
            raise ValueError("ID inválido (não pode ser None ou vazio)")

    def set_nome(self, nome):
        try:
            if nome is None or nome.strip() == "":
                raise ValueError
            self.__nome = nome
        except Exception:
            raise ValueError("Nome inválido (não pode ser vazio)")

    def set_email(self, email):
        try:
            if email is None or email.strip() == "":
                raise ValueError
            self.__email = email
        except Exception:
            raise ValueError("E-mail inválido (não pode ser vazio)")

    def set_fone(self, fone):
        try:
            if fone is None or fone.strip() == "":
                raise ValueError
            self.__fone = fone
        except Exception:
            raise ValueError("Fone inválido (não pode ser vazio)")

    def set_senha(self, senha):
        try:
            if senha is None or senha.strip() == "":
                raise ValueError
            self.__senha = senha
        except Exception:
            raise ValueError("Senha inválida (não pode ser vazia)")

    # serialização / desserialização
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
        except (FileNotFoundError, json.JSONDecodeError):
            cls.__objetos = []

    @classmethod
    def salvar(cls):
        with open(cls.arquivo, mode="w", encoding="utf-8") as arquivo:
            json.dump([obj.to_json() for obj in cls.__objetos], arquivo, indent=4, ensure_ascii=False)

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id_max = 0
        for aux in cls.__objetos:
            try:
                if aux.get_id() > id_max:
                    id_max = aux.get_id()
            except Exception:
                pass
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
        cls.__objetos.append(obj)
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cls.__objetos = [aux for aux in cls.__objetos if aux.get_id() != obj.get_id()]
        cls.salvar()
