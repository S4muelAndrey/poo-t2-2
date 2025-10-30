import json
from models.dao import DAO
from datetime import datetime

class Horario:
    def __init__(self, id, data):
        self.__id = id
        self.set_data(data)
        self.__confirmado = False
        self.__id_cliente = None
        self.__id_servico = None
        self.__id_profissional = None

    # getters
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    # setters
    def set_data(self, data):
            if data is None:
                raise ValueError("Data inválida")
            if isinstance(data, str):
                data = datetime.fromisoformat(data)
            if data.year < 2025:
                raise ValueError("Ano deve ser após 2025.")
            self.__data = data

    def set_confirmado(self, confirmado): 
        try:
            if confirmado == None: raise ValueError("Confirmado deve ser True ou False")
            self.__confirmado = confirmado
        except Exception as Erro: raise ValueError(Erro)

    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_dict(self):
        """Converte o objeto em dicionário serializável"""
        data_str = None
        if isinstance(self.__data, datetime):
            data_str = self.__data.strftime("%Y-%m-%d %H:%M:%S")
        elif isinstance(self.__data, str):
            data_str = self.__data
        else:
            data_str = str(self.__data)
        return {
            "id": self.__id,
            "data": data_str,
            "confirmado": self.__confirmado,
            "id_cliente": self.__id_cliente,
            "id_servico": self.__id_servico,
            "id_profissional": self.__id_profissional
        }


    def __str__(self):
        if isinstance(self.__data, datetime):
            return self.__data.strftime("%d/%m/%Y %H:%M")
        return str(self.__data)

    @staticmethod
    def from_dict(d):
        """Reconstrói um objeto Horario a partir de um dicionário"""
        data = d.get("data")
        # converte para datetime se possível
        if isinstance(data, str):
            for fmt in ("%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%Y-%m-%dT%H:%M:%S"):
                try:
                    data = datetime.strptime(data, fmt)
                    break
                except:
                    pass
        h = Horario(d.get("id"), data)
        h.set_confirmado(d.get("confirmado", False))
        h.set_id_cliente(d.get("id_cliente"))
        h.set_id_servico(d.get("id_servico"))
        h.set_id_profissional(d.get("id_profissional"))
        return h


class HorarioDAO(DAO):
    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default = Horario.to_json)

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls._objetos.append(obj)

        except FileNotFoundError:
            pass