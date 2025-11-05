import json
from models.dao import DAO

class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def get_id(self): return self.__id
    def get_descricao(self): return self.__descricao
    def get_valor(self): return self.__valor

    def set_id(self, id):
        try: 
            if id is None or id == "": raise ValueError("ID não pode ser vazio")
            self.__id = id
        except Exception as Erro: raise ValueError(Erro)

    def set_descricao(self, descricao):
        try:
            if descricao is None or descricao =="": raise ValueError("Descrição não pode ser vazio")
            self.__descricao = descricao
        except Exception as Erro: raise ValueError(Erro)

    def set_valor(self, valor):
        try:
            if valor is None or int(valor.strip()) < 0: raise ValueError("Valor deve ser maior que 0")
        except Exception as Erro: raise ValueError(Erro)

    def to_json(self):
        dic = {"id":self.__id, "descricao":self.__descricao, "valor":self.__valor}
        return dic
    
    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])

    def __str__(self):
        return f"{self.__id} - {self.__descricao} - {self.__valor}"

class ServicoDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Servico.to_json)

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls._objetos.append(obj)

        except FileNotFoundError:
            pass