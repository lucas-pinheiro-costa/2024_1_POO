'''
Escrever a classe Paciente de acordo com o diagrama UML apresentado.
A classe deve utilizar os atributos nome, cpf, telefone e nascimento usados no registro de dados dos pacientes de uma clínica. O construtor da classe deve receber os valores iniciais dos dados de um paciente. O método Idade deve retornar um texto com a idade do paciente em anos e meses, de acordo com a sua data de nascimento e a data atual. O método ToString deve retornar um texto com os atributos do objeto.
'''

from datetime import datetime

class Paciente:

    # Método construtor dos atributos da classe Paciente
    def __init__(self, nome, cpf, telefone, nascimento):
        self.__nome = nome.capitalize()
        self.__cpf = cpf
        self.__telefone = telefone
        self.__nascimento = datetime.strptime(nascimento, "%d/%m/%Y")

    def get_nome(self):
        return self.__nome

    # Método idade() serve para retornar um texto com a idade do paciente em anos e meses
    def idade(self):
        
        # Implementar o código que calcula a idade do paciente

    # Métodos ToString para retornar um texto com os dados do paciente
    def __str__(self):
        return f"Nome: {self.__nome} \nCPF: {self.__cpf} \nTelefone de contato: {self.__telefone} \nData de nascimento: {self.__nascimento.strftime('%d/%m/%Y')}\n"


class UI:
    @staticmethod
    def main():
        print("\n\tAPLICATIVO DE CADASTRO DE PACIENTES")
        lista_pacientes = []

        while True:
            print("\n1 - Cadastrar um novo paciente")
            print("2 - Excluir um paciente cadastrado")
            print("3 - Listar todos os pacientes cadastrados")
            print("4 - Exibir dados de um paciente específico")
            print("5 - Exibir idade de um paciente")
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
                print("Pacientes cadastrados:")
                for i, paciente in enumerate(lista_pacientes):
                    print(f"{i + 1} - {paciente.get_nome()}")
                try:
                    index = int(input("Escolha o número do paciente: ")) - 1
                    paciente = lista_pacientes[index]
                    print(f"Deseja excluir o cadastro do paciente '{paciente.get_nome()}'?")
                    resposta = input("(S/N): ")
                    if resposta.upper() == 'S':
                        del lista_pacientes[index]
                        print(f"Cadastro do paciente '{paciente.get_nome()}' excluído com sucesso.")
                    else:
                        print("Operação cancelada.")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '3':  # Listar todos os pacientes cadastrados
                print("\Pacientes cadastradas:")
                for i, empresa in enumerate(empresas):
                    print(f"{i + 1} - {empresa.get_nome()}")
            
            elif operation == '4':  # Listar clientes de uma empresa
                if not empresas:
                    print("Nenhuma empresa criada ainda.")
                    continue
                print("Empresas disponíveis:")
                for i, empresa in enumerate(empresas):
                    print(f"{i + 1} - {empresa.get_nome()}")
                try:
                    index = int(input("Escolha o número da empresa: ")) - 1
                    empresa = empresas[index]
                    print(f"\nClientes da empresa '{empresa.get_nome()}':")
                    for cliente in empresa.listar():
                        print(cliente)
                except (ValueError, IndexError):
                    print("Opção inválida.")
            
            elif operation == '9':  # Sair
                break
            
            else:
                print("Opção inválida.")

        print("Fim do programa.")


UI.main()
