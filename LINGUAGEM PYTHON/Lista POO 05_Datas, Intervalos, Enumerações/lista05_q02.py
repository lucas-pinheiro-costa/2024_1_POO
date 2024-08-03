'''
Escrever a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo. A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores e situação de pagamento. O construtor da classe recebe os dados iniciais de um boleto. O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto. O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o valor do pagamento corresponder ao valor do boleto. O método ToString deve retornar um texto com os atributos do objeto. A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
'''

############### O CÓDIGO ABAIXO FOI REUTILIZADO DA QUESTÃO 01, TEM QUE FAZER ALTERAÇÕES

from datetime import datetime
from enum import Enum

class Boleto:
    # Método construtor dos atributos da classe Boleto
    def __init__(self, codBarras, dataEmissao, dataVencimento, dataPagto, valorBoleto):
        self.__codBarras = codBarras
        self.__dataEmissao = datetime.strptime(dataEmissao, "%d/%m/%Y")
        self.__dataVencimento = datetime.strptime(dataVencimento, "%d/%m/%Y")
        self.__dataPagto = datetime.strptime(dataPagto, "%d/%m/%Y")
        self.__valorBoleto = valorBoleto
        
    # Método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto.
    def pagar(self, valorPago):
        self.__valorPago = valorPago
        
    # Método Situação retorna a situação de pagamento do boleto.
    def situacao(self):
        if self.__valorPago is None:
            return Pagamento.EmAberto
        elif self.__valorPago < self.__valorBoleto:
            return Pagamento.PagoParcial
        else:
            return Pagamento.Pago

    # Métodos ToString para retornar um texto com os dados do Boleto
    def __str__(self):
        return f"O boleto possui os seguintes dados:\n\tCódigo de barra: {self.__codBarras}\n\tData de emissão: {self.__dataEmissao.strftime('%d/%m/%Y')}\n\tData de vencimento: {self.__dataVencimento.strftime('%d/%m/%Y')}\n\tData do pagamento: {self.__dataPagto.strftime('%d/%m/%Y')}\n\tValor do boleto: R$ {self.__valorBoleto}\n\tValor pago: R$ {self.__valorPago if self.__valorPago is not None else 'N/A'}\n\tSituação do pagamento: {self.situacao().name}"
    
class Pagamento(Enum):
    EmAberto = 1
    PagoParcial = 2
    Pago = 3


class UI:
    @staticmethod
    def main():
        print("\n\tINFORMES DE BOLETO BANCÁRIO")

        while True:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print("1 - Cadastrar um novo boleto")
            print("2 - Realizar o pagamento de um boleto")
            print("3 - Verificar a situação do boleto")
            print("4 - Verificar os dados do boleto")
            print("9 - Sair")

            operation = input("Escolha uma opção: ")

            if operation == '1':    # Cadastrar um novo Boleto
                codBarras = input("Digite o codBarras completo do Boleto: ")
                cpf = input("Digite o CPF do Boleto no formato 'XXX.XXX.XXX-XX': ")
                telefone = input("Digite o telefone de contato do Boleto: ")
                dataEmissao = input("Digite a data de dataEmissao do Boleto no formato 'DD/MM/YYYY': ")
                Boleto = Boleto(codBarras, cpf, telefone, dataEmissao)
                lista_Boletos.append(Boleto)
                print(f"Boleto '{codBarras}' cadastrado com sucesso.")
            
            elif operation == '2':  # Excluir um Boleto cadastrado
                if not lista_Boletos:
                    print("Nenhum Boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, Boleto in enumerate(lista_Boletos):
                    print(f"{i + 1} - {Boleto.get_codBarras()}")
                try:
                    index = int(input("\nEscolha o número do Boleto: ")) - 1
                    Boleto = lista_Boletos[index]
                    print(f"Deseja excluir o cadastro do Boleto '{Boleto.get_codBarras()}'?\t")
                    resposta = input("(S/N): ")
                    if resposta.upper() == 'S':
                        print(f"Cadastro do Boleto '{Boleto.get_codBarras()}' excluído com sucesso.")
                        del lista_Boletos[index]
                    else:
                        print("Operação cancelada.")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '3':  # Listar todos os Boletos cadastrados
                if not lista_Boletos:
                    print("Nenhum Boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, Boleto in enumerate(lista_Boletos):
                    print(f"{i + 1} - {Boleto.get_codBarras()}")
            
            elif operation == '4':  # Exibir dados de um Boleto específico
                if not lista_Boletos:
                    print("Nenhum Boleto cadastrado ainda.")
                    continue
                print("\nBoletos cadastrados:")
                for i, Boleto in enumerate(lista_Boletos):
                    print(f"{i + 1} - {Boleto.get_codBarras()}")
                try:
                    index = int(input("\nEscolha o número do Boleto: ")) - 1
                    Boleto = lista_Boletos[index]
                    print(f"Seguem abaixo os dados do Boleto '{Boleto.get_codBarras()}':")
                    print(Boleto)
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '9':  # Sair
                break
            
            else:
                print("Opção inválida.")

        print("\nFim do programa.")

UI.main()