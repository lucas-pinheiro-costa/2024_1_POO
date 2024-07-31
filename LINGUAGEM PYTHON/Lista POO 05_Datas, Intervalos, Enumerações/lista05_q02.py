'''
Escrever a classe Boleto e a enumeração Pagamento de acordo com o diagrama UML apresentado abaixo. A classe deve ter como atributos os dados de um boleto com informações sobre código de barras, datas, valores e situação de pagamento. O construtor da classe recebe os dados iniciais de um boleto. O método Pagar registra o valor pago para o boleto que pode ser menor ou igual ao valor do boleto. O método Situacao retorna a situação de pagamento do boleto que pode ser: Em Aberto, quando o pagamento ainda não foi realizado; Pago Parcial, quando o valor pago for menor que o valor do boleto; ou Pago, quando o valor do pagamento corresponder ao valor do boleto. O método ToString deve retornar um texto com os atributos do objeto. A enumeração Pagamento é usada para listar os possíveis valores das situações de pagamento de um boleto.
'''

############### O CÓDIGO ABAIXO FOI REUTILIZADO DA QUESTÃO 01

from datetime import datetime

class Paciente:
    # Método construtor dos atributos da classe Paciente
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome.upper()
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def get_nome(self):
        return self.__nome

    # Método idade() serve para retornar um texto com a idade do paciente em anos e meses
    def idade(self):
        hoje = datetime.today()
        anos = hoje.year - self.__nascimento.year
        meses = hoje.month - self.__nascimento.month
        if meses < 0:
            anos -= 1
            meses += 12
        return f"{anos} anos e {meses} meses."

    # Métodos ToString para retornar um texto com os dados do paciente
    def __str__(self):
        return f"Nome: {self.__nome}\nCPF: {self.__cpf}\nTelefone de contato: {self.__telefone}\nData de nascimento: {self.__nascimento.strftime('%d/%m/%Y')}"


class UI:
    @staticmethod
    def main():
        print("\n\tAPLICATIVO DE CADASTRO DE PACIENTES")
        lista_pacientes = []

        while True:
            print("\n:::::::::::::::::::::::::::::::::::::::")
            print("1 - Cadastrar um novo paciente")
            print("2 - Excluir um paciente cadastrado")
            print("3 - Listar todos os pacientes cadastrados")
            print("4 - Exibir dados de um paciente específico")
            print("5 - Exibir a idade de um paciente")
            print("9 - Sair")

            operation = input("Escolha uma opção: ")

            if operation == '1':    # Cadastrar um novo paciente
                nome = input("Digite o nome completo do paciente: ")
                cpf = input("Digite o CPF do paciente no formato 'XXX.XXX.XXX-XX': ")
                telefone = input("Digite o telefone de contato do paciente: ")
                nascimento = input("Digite a data de nascimento do paciente no formato 'DD/MM/YYYY': ")
                paciente = Paciente(nome, cpf, telefone, nascimento)
                lista_pacientes.append(paciente)
                print(f"Paciente '{nome}' cadastrado com sucesso.")
            
            elif operation == '2':  # Excluir um paciente cadastrado
                if not lista_pacientes:
                    print("Nenhum paciente cadastrado ainda.")
                    continue
                print("\nPacientes cadastrados:")
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i + 1} - {paciente.get_nome()}")
                try:
                    index = int(input("\nEscolha o número do paciente: ")) - 1
                    paciente = lista_pacientes[index]
                    print(f"Deseja excluir o cadastro do paciente '{paciente.get_nome()}'?\t")
                    resposta = input("(S/N): ")
                    if resposta.upper() == 'S':
                        print(f"Cadastro do paciente '{paciente.get_nome()}' excluído com sucesso.")
                        del lista_pacientes[index]
                    else:
                        print("Operação cancelada.")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '3':  # Listar todos os pacientes cadastrados
                if not lista_pacientes:
                    print("Nenhum paciente cadastrado ainda.")
                    continue
                print("\nPacientes cadastrados:")
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i + 1} - {paciente.get_nome()}")
            
            elif operation == '4':  # Exibir dados de um paciente específico
                if not lista_pacientes:
                    print("Nenhum paciente cadastrado ainda.")
                    continue
                print("\nPacientes cadastrados:")
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i + 1} - {paciente.get_nome()}")
                try:
                    index = int(input("\nEscolha o número do paciente: ")) - 1
                    paciente = lista_pacientes[index]
                    print(f"Seguem abaixo os dados do paciente '{paciente.get_nome()}':")
                    print(paciente)
                except (ValueError, IndexError):
                    print("Opção inválida.")
                    
            elif operation == '5':  # Exibir a idade de um paciente
                if not lista_pacientes:
                    print("Nenhum paciente cadastrado ainda.")
                    continue
                print("\nPacientes cadastrados:")
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i + 1} - {paciente.get_nome()}")
                try:
                    index = int(input("\nEscolha o número do paciente: ")) - 1
                    paciente = lista_pacientes[index]
                    print(f"Idade do paciente '{paciente.get_nome()}': {paciente.idade()}")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '9':  # Sair
                break
            
            else:
                print("Opção inválida.")

        print("\nFim do programa.")

UI.main()