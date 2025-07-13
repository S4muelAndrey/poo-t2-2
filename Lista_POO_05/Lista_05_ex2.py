import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.__codBarras = codBarras
        self.__dataEmissao = dataEmissao
        self.__dataVencimento = dataVencimento
        self.__valorBoleto = valorBoleto
        self.__dataPago = None
        self.__valorPago = 0.0
        self.__situacaoPagamento = Pagamento.EmAberto

    def pagar(self, valorPago):
        if valorPago <= 0:
            raise ValueError("O valor pago deve ser maior que zero.")
        
        self.__valorPago += valorPago
        self.__dataPago = datetime.datetime.now()

        if self.__valorPago == 0:
            self.__situacaoPagamento = Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            self.__situacaoPagamento = Pagamento.PagoParcial
        else:
            self.__situacaoPagamento = Pagamento.Pago

    def situacao(self):
        return self.__situacaoPagamento

    def get_codBarras(self):
        return self.__codBarras

    def get_dataEmissao(self):
        return self.__dataEmissao

    def get_dataVencimento(self):
        return self.__dataVencimento

    def get_dataPago(self):
        return self.__dataPago

    def get_valorBoleto(self):
        return self.__valorBoleto

    def get_valorPago(self):
        return self.__valorPago

    def get_situacaoPagamento(self):
        return self.__situacaoPagamento

    def set_valorBoleto(self, valor):
        if valor > 0:
            self.__valorBoleto = valor
        else:
            raise ValueError("Valor do boleto deve ser maior que zero.")

    def __str__(self):
        return (f"Boleto:\n"
                f"Código de Barras: {self.__codBarras}\n"
                f"Emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}\n"
                f"Vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\n"
                f"Valor do Boleto: R$ {self.__valorBoleto:.2f}\n"
                f"Valor Pago: R$ {self.__valorPago:.2f}\n"
                f"Data do Pagamento: {self.__dataPago.strftime('%d/%m/%Y %H:%M') if self.__dataPago else 'Não pago'}\n"
                f"Situação: {self.__situacaoPagamento.name}")


class BoletoUI:
    def __init__(self):
        self.__boletos = []

    def menu(self):
        while True:
            print("\n=== MENU BOLETOS ===")
            print("1. Cadastrar novo boleto")
            print("2. Listar boletos")
            print("3. Registrar pagamento")
            print("4. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.__cadastrar()
            elif opcao == "2":
                self.__listar()
            elif opcao == "3":
                self.__registrar_pagamento()
            elif opcao == "4":
                print("Encerrando sistema de boletos...")
                break
            else:
                print("Opção inválida!")

    def __cadastrar(self):
        try:
            cod = input("Código de Barras: ")
            emissao = input("Data de Emissão (YYYY-MM-DD): ")
            venc = input("Data de Vencimento (YYYY-MM-DD): ")
            valor = float(input("Valor do Boleto (R$): "))

            data_emissao = datetime.datetime.strptime(emissao, "%Y-%m-%d")
            data_venc = datetime.datetime.strptime(venc, "%Y-%m-%d")
            boleto = Boleto(cod, data_emissao, data_venc, valor)

            self.__boletos.append(boleto)
            print("\n--- Boleto cadastrado ---")
            print(boleto)

        except ValueError as e:
            print(f"Erro: {e}")

    def __listar(self):
        if not self.__boletos:
            print("Nenhum boleto cadastrado.")
        else:
            for b in self.__boletos:
                print("-" * 30)
                print(b)

    def __registrar_pagamento(self):
        cod = input("Informe o código de barras do boleto: ")
        for b in self.__boletos:
            if b.get_codBarras() == cod:
                try:
                    valor = float(input("Valor pago (R$): "))
                    b.pagar(valor)
                    print("\n--- Pagamento registrado ---")
                    print(b)
                except ValueError as e:
                    print(f"Erro ao pagar: {e}")
                return
        print("Boleto não encontrado.")

    @staticmethod
    def executar():
        BoletoUI.main()

    @staticmethod
    def main():
        app = BoletoUI()
        app.menu()


if __name__ == "__main__":
    BoletoUI.executar()
