'''
Escrever as classes Empresa e Cliente, usadas para cadastrar os clientes de uma empresa de cartões de crédito,
de acordo com o diagrama UML apresentado.
• Cada empresa deve ter um nome e uma lista de clientes;
• O construtor da classe Empresa recebe o nome da empresa e possui métodos recuperar e alterar esse valor
(get/set);
• A classe define as seguintes operações: Inserir, para cadastrar um cliente e Listar, para retornar uma lista com
os clientes já cadastrados;
• A classe Cliente modela um cliente que deve possuir nome, cpf e limite de crédito;
• Um cliente pode também ter um sócio, também cliente. Nesta situação, o seu limite de crédito deve ser somado
ao limite de crédito de seu sócio e vice-versa;
• A sociedade deve acontecer em pares, ou seja, quando um cliente A for sócio de um cliente B, B deve ser sócio
de A;
• O construtor da classe recebe os dados iniciais do cliente;
• O método SetSocio é usado para definir a sociedade entre dois clientes;
• O método GetLimite retorna o limite do cliente, considerando o limite de seu sócio quando existir;
• O método ToString retorna um texto com os dados do cliente;
• Insira outros atributos e métodos nas classes, caso necessário.
'''

class Empresa:

    # Método construtor dos atributos da classe Empresa
    def __init__(self, nome):
        self.__nome = nome.capitalize()
        self.__clientes = []

    # Métodos getter/setter do atributo Empresa.__nome
    def get_nome(self):
        return self.__nome
    def set_nome(self, nome):
        self.__nome = nome.capitalize()

    def inserir(self, cliente):
        self.__clientes.append(cliente)

    def listar(self):   # Método Listar funciona como um __str__ (ToString) para o atributo Empresa.__clientes []
        return self.__clientes


class Cliente:

    # Método construtor dos atributos da classe Cliente
    def __init__(self, nome, cpf, limite_credito):
        self.__nome = nome.capitalize()
        self.__cpf = cpf
        self.__limite_credito = limite_credito
        self.__socio = None

    # Método setter do atributo Empresa.__socio para fazer sociedade entre dois clientes
    def set_socio(self, socio):
        if isinstance(socio, Cliente):  # No método set_socio() da classe Cliente, é necessário verificar se o parâmetro passado como sócio é realmente uma instância da classe Cliente.
            self.__socio = socio
            socio.__socio = self

    # Método getter do atributo Empresa.__limite_credito para unir os limites de dois sócios (clientes)
    def get_limite(self):
        limite_total = self.__limite_credito
        if self.__socio:
            limite_total += self.__socio.__limite_credito
        return limite_total

    # Métodos ToString do atributo Empresa.__socio para retornar um texto com os dados do cliente
    def __str__(self):
        if self.__socio:
            return f"Nome: {self.__nome}, CPF: {self.__cpf}, Limite de Crédito: {self.get_limite():.2f}, Sócio: {self.__socio.__nome}"
        else:
            return f"Nome: {self.__nome}, CPF: {self.__cpf}, Limite de Crédito: {self.get_limite():.2f}, Sócio: Nenhum"


class UI:
    @staticmethod
    def main():
        print("\n\tAPLICATIVO DE CADASTRO DE CLIENTES")
        empresas = []

        while True:
            print("\n1 - Criar nova empresa")
            print("2 - Adicionar cliente a uma empresa existente")
            print("3 - Listar todas as empresas")
            print("4 - Listar clientes de uma empresa")
            print("9 - Sair")

            operation = input("Escolha uma opção: ")

            if operation == '1':    # Criar nova empresa
                nome = input("Digite o nome da nova empresa: ")
                empresa = Empresa(nome)
                empresas.append(empresa)
                print(f"Empresa '{nome}' criada com sucesso.")
            elif operation == '2':  # Adicionar cliente a uma empresa existente
                if not empresas:
                    print("Nenhuma empresa criada ainda.")
                    continue
                print("Empresas disponíveis:")
                for i, empresa in enumerate(empresas):
                    print(f"{i + 1} - {empresa.get_nome()}")
                try:
                    index = int(input("Escolha o número da empresa: ")) - 1
                    empresa = empresas[index]
                    nome = input("Digite o nome do cliente: ")
                    cpf = input("Digite o CPF do cliente no formato 'XXX.XXX.XXX-XX': ")
                    limite_credito = float(input("Digite o limite de crédito do cliente: "))
                    cliente = Cliente(nome, cpf, limite_credito)
                    empresa.inserir(cliente)
                    print(f"Cliente '{nome}' adicionado à empresa '{empresa.get_nome()}'.")
                except (ValueError, IndexError):
                    print("Opção inválida.")
            elif operation == '3':  # Listar todas as empresas
                print("\nEmpresas cadastradas:")
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





'''# Teste das classes
empresa = Empresa("EmpresaX")

cliente1 = Cliente("João", "123.456.789-00", 1000.00)
cliente2 = Cliente("Maria", "987.654.321-00", 1500.00)

cliente1.set_socio(cliente2)

empresa.inserir(cliente1)
empresa.inserir(cliente2)

clientes_cadastrados = empresa.listar()
for cliente in clientes_cadastrados:
    print(cliente)
'''