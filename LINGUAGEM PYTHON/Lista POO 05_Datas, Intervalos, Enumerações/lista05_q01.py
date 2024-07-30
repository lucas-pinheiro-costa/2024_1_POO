'''
Escrever a classe Paciente de acordo com o diagrama UML apresentado.
A classe deve utilizar os atributos nome, cpf, telefone e nascimento usados no registro de dados dos pacientes de uma clínica. O construtor da classe deve receber os valores iniciais dos dados de um paciente. O método Idade deve retornar um texto com a idade do paciente em anos e meses, de acordo com a sua data de nascimento e a data atual. O método ToString deve retornar um texto com os atributos do objeto.
'''

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