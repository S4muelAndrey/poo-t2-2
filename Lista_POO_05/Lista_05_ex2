
import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.codBarras = codBarras
        self.dataEmissao = dataEmissao
        self.dataVencimento = dataVencimento
        self.valorBoleto = valorBoleto
        self.dataPago = None
        self.valorPago = 0.0
        self.situacaoPagamento = Pagamento.EmAberto

    def pagar(self, valorPago):
        if valorPago <= 0:
            raise ValueError("O valor pago deve ser maior que zero.")
        
        self.valorPago += valorPago
        self.dataPago = datetime.datetime.now()

        if self.valorPago == 0:
            self.situacaoPagamento = Pagamento.EmAberto
        elif self.valorPago < self.valorBoleto:
            self.situacaoPagamento = Pagamento.PagoParcial
        elif self.valorPago >= self.valorBoleto:
            self.situacaoPagamento = Pagamento.Pago

    def situacao(self):
        return self.situacaoPagamento

    def get_codBarras(self):
        return self.codBarras

    def get_dataEmissao(self):
        return self.dataEmissao

    def get_dataVencimento(self):
        return self.dataVencimento

    def get_dataPago(self):
        return self.dataPago

    def get_valorBoleto(self):
        return self.valorBoleto

    def get_valorPago(self):
        return self.valorPago

    def get_situacaoPagamento(self):
        return self.situacaoPagamento

    def set_valorBoleto(self, valor):
        if valor > 0:
            self.valorBoleto = valor
        else:
            raise ValueError("Valor do boleto deve ser maior que zero.")

    def __str__(self):
        return (f"Boleto:\n"
                f"Código de Barras: {self.codBarras}\n"
                f"Emissão: {self.dataEmissao.strftime('%d/%m/%Y')}\n"
                f"Vencimento: {self.dataVencimento.strftime('%d/%m/%Y')}\n"
                f"Valor do Boleto: R$ {self.valorBoleto:.2f}\n"
                f"Valor Pago: R$ {self.valorPago:.2f}\n"
                f"Data do Pagamento: {self.dataPago.strftime('%d/%m/%Y %H:%M') if self.dataPago else 'Não pago'}\n"
                f"Situação: {self.situacaoPagamento.name}")


def boletoUI():
    print("=== Cadastro de Boleto ===")
    cod = input("Código de Barras: ")
    emissao = input("Data de Emissão (YYYY-MM-DD): ")
    venc = input("Data de Vencimento (YYYY-MM-DD): ")
    valor = float(input("Valor do Boleto (R$): "))

    try:
        data_emissao = datetime.datetime.strptime(emissao, "%Y-%m-%d")
        data_venc = datetime.datetime.strptime(venc, "%Y-%m-%d")
        boleto = Boleto(cod, data_emissao, data_venc, valor)

        print("\n--- Dados do Boleto ---")
        print(boleto)

        opcao = input("\nDeseja registrar um pagamento? (s/n): ").lower()
        if opcao == 's':
            valor_pagamento = float(input("Valor pago (R$): "))
            boleto.pagar(valor_pagamento)
            print("\n--- Situação Atualizada ---")
            print(boleto)

    except ValueError as e:
        print(f"Erro: {e}")

boletoUI()
