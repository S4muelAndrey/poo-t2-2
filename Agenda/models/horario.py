import json
from models.dao import DAO
from datetime import datetime

class Horario:
    def __init__(self, id, data, urgencia):
        self.set_id(id)
        self.set_data(data)
        self.set_urgencia(urgencia)
        self.__confirmado = False
        self.__id_cliente = None
        self.__id_servico = None
        self.__id_profissional = None

    # getters
    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_urgencia(self) : return self.__urgencia
    def get_confirmado(self): return self.__confirmado
    def get_id_cliente(self): return self.__id_cliente
    def get_id_servico(self): return self.__id_servico
    def get_id_profissional(self): return self.__id_profissional

    # setters
    def set_id(self, id): 
        if id is None:
            raise ValueError("ID inválido")
        self.__id = id


    def set_data(self, data):
        if data is None:
            raise ValueError("Data inválida")
        if isinstance(data, str):
            data = datetime.fromisoformat(data)
        if data.year < 2025:
            raise ValueError("Ano deve ser após 2025.")
        self.__data = data

    def set_urgencia(self, urgencia):
        if urgencia in (None, ""):
            # Pode ser None ou vazio → define como None
            self.__urgencia = None
            return
        try:
            urg = int(urgencia)
        except (TypeError, ValueError):
            raise ValueError("Urgência deve ser um número inteiro entre 1 e 3, ou None")

        if urg < 1 or urg > 3:
            raise ValueError("Urgência deve ser um número inteiro entre 1 e 3")

        self.__urgencia = urg



    def set_confirmado(self, confirmado): 
        try:
            if confirmado == None: raise ValueError("Confirmado deve ser True ou False")
        except Exception as Erro: raise ValueError(Erro)
        self.__confirmado = confirmado

    def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
    def set_id_servico(self, id_servico): self.__id_servico = id_servico
    def set_id_profissional(self, id_profissional): self.__id_profissional = id_profissional

    def to_dict(self):
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
            "urgencia": self.__urgencia,  
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
        urgencia = d.get("urgencia", None)
        h = Horario(d.get("id"), data, urgencia)
        h.set_confirmado(d.get("confirmado", False))
        h.set_id_cliente(d.get("id_cliente"))
        h.set_id_servico(d.get("id_servico"))
        h.set_id_profissional(d.get("id_profissional"))
        return h
    
    @staticmethod
    def to_json(self):
        dic = {"id":self.__id, "data":self.__data.strftime("%d/%m/%Y %H:%M"), "urgencia":self.__urgencia, "confirmado":self.__confirmado, "id_cliente":self.__id_cliente, "id_servico":self.__id_servico, "id_profissional":self.__id_profissional}
        return dic

    @staticmethod
    def from_json(dic):
        data = dic["data"]

        if isinstance(data, str):
            for fmt in ("%d/%m/%Y %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"):
                try:
                    data = datetime.strptime(data, fmt)
                    break
                except ValueError:
                    continue
            else:
                raise ValueError(f"Formato de data inválido: {data}")

        horario = Horario(dic["id"], data, dic.get("urgencia"))
        horario.set_confirmado(dic.get("confirmado", False))
        horario.set_id_cliente(dic.get("id_cliente"))
        horario.set_id_servico(dic.get("id_servico"))
        horario.set_id_profissional(dic.get("id_profissional"))
        return horario



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