'''
Escrever a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo. A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores e situação de pagamento. O construtor da classe recebe os dados iniciais de um boleto. O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto. O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o valor do pagamento corresponder ao valor do boleto. O método ToString deve retornar um texto com os atributos do objeto. A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
'''

from datetime import datetime
from enum import Enum

class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3

class Boleto:
    # Método construtor dos atributos da classe Boleto
    def __init__(self, codBarras, dataEmissao, dataVencimento, valorBoleto):
        self.__codBarras = codBarras
        self.__dataEmissao = datetime.strptime(dataEmissao, "%d/%m/%Y")
        self.__dataVencimento = datetime.strptime(dataVencimento, "%d/%m/%Y")
        self.__dataPagto = None
        self.__valorBoleto = valorBoleto
        self.__valorPago = 0.0

    def get_codBarras(self):
        return self.__codBarras

    def pagar(self, valorPago):
        if self.__valorPago + valorPago <= self.__valorBoleto:
            self.__valorPago += valorPago
            self.__dataPagto = datetime.now()
        else:
            print("O valor pago excede o valor do boleto.")
        
    def situacao(self):
        if self.__valorPago == 0:
            return Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            return Pagamento.PagoParcial
        else:
            return Pagamento.Pago

    def __str__(self):
        data_pagto = self.__dataPagto.strftime('%d/%m/%Y') if self.__dataPagto else 'N/A'
        return (f"O boleto possui os seguintes dados:\n"
                f"\tCódigo de barra: {self.__codBarras}\n"
                f"\tData de emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}\n"
                f"\tData de vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\n"
                f"\tData do pagamento: {data_pagto}\n"
                f"\tValor do boleto: R$ {self.__valorBoleto:.2f}\n"
                f"\tValor pago: R$ {self.__valorPago:.2f}\n"
                f"\tSituação do pagamento: {self.situacao().name}")

class UI:
    @staticmethod
    def main():
        print("\n\tINFORMES DE BOLETO BANCÁRIO")
        lista_boletos = []

        while True:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print("1 - Cadastrar um novo boleto")
            print("2 - Realizar o pagamento de um boleto")
            print("3 - Verificar a situação do boleto")
            print("4 - Verificar os dados do boleto")
            print("9 - Sair")

            operation = input("Escolha uma opção: ")

            if operation == '1':    # Cadastrar um novo Boleto
                codBarras = input("Digite o código de barras do boleto: ")
                dataEmissao = input("Digite a data de emissão do boleto no formato 'DD/MM/YYYY': ")
                dataVencimento = input("Digite a data de vencimento do boleto no formato 'DD/MM/YYYY': ")
                valorBoleto = float(input("Digite o valor do boleto: "))
                boleto = Boleto(codBarras, dataEmissao, dataVencimento, valorBoleto)
                lista_boletos.append(boleto)
                print(f"Boleto '{codBarras}' cadastrado com sucesso.")
            
            elif operation == '2':  # Realizar o pagamento de um Boleto
                if not lista_boletos:
                    print("Nenhum boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, boleto in enumerate(lista_boletos):
                    print(f"{i + 1} - {boleto.get_codBarras()}")
                try:
                    index = int(input("\nEscolha o número do boleto: ")) - 1
                    boleto = lista_boletos[index]
                    valorPago = float(input("Digite o valor a ser pago: "))
                    boleto.pagar(valorPago)
                    print(f"Pagamento de R$ {valorPago:.2f} realizado para o boleto '{boleto.get_codBarras()}'.")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '3':  # Verificar a situação do boleto
                if not lista_boletos:
                    print("Nenhum boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, boleto in enumerate(lista_boletos):
                    print(f"{i + 1} - {boleto.get_codBarras()}")
                try:
                    index = int(input("\nEscolha o número do boleto: ")) - 1
                    boleto = lista_boletos[index]
                    print(f"A situação do boleto '{boleto.get_codBarras()}' é: {boleto.situacao().name}")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '4':  # Verificar os dados do boleto
                if not lista_boletos:
                    print("Nenhum boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, boleto in enumerate(lista_boletos):
                    print(f"{i + 1} - {boleto.get_codBarras()}")
                try:
                    index = int(input("\nEscolha o número do boleto: ")) - 1
                    boleto = lista_boletos[index]
                    print(f"\nDados do boleto '{boleto.get_codBarras()}':")
                    print(boleto)
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '9':  # Sair
                break
            
            else:
                print("Opção inválida.")

        print("\nFim do programa.")

UI.main()