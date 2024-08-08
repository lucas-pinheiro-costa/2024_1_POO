import datetime

class Cliente:
    def __init__(self, id, n, e, f):
        self.__id = id
        self.__nome = n
        self.__email = e
        self.__fone = f
        #if not isinstance(id, int): raise ValueError("\nO ID não é um valor inteiro.") # o usuário já informou um valor string que foi convertido para int no método cliente_inserir()
        
        if (id <= 0): raise ValueError("\nID inválido, informe outro número.")
        if (n == ""): raise ValueError("\nO campo nome precisa ser preenchido")
        if (e == ""): raise ValueError("\nO campo e-mail precisa ser preenchido") 
        if (f == ""): raise ValueError("\nO campo Telefone precisa ser preenchido")
    
    def __str__(self):
        return f"ID nº {self._id}\n\tNome do cliente: {self._nome}\n\tE-mail: {self._email}\n\tTelefone: {self._fone}"

    def set_id(self, id):
        if (id <= 0): raise ValueError("\nID inválido, informe outro número.")
        self.__id = id
    
    def set_nome(self, n):
        if (n == ""): raise ValueError("\nO campo nome precisa ser preenchido")
        self.__nome = n

    def set_email(self, e):
        if (e == ""): raise ValueError("\nO campo e-mail precisa ser preenchido")
        self.__email = e
    
    def set_fone(self, f):
        if (f == ""): raise ValueError("\nO campo Telefone precisa ser preenchido")
        self.__fone = f
    
    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email
    
    def get_fone(self):
        return self.__fone
    
class Venda:
    def __init__(self, id):
        self._id = id
        self._data = self._data
        self._carrinho = self._carrinho
        self._total = self._total
        self._idCliente = Cliente.get_id()
    
    def get_id(self):
        return self.__id

    def get_data(self):
        return self.__data

    def get_carrinho(self):
        return self.__carrinho

    def get_total(self):
        return self.__total

    def get_idCliente(self):
        return self.__idCliente
    
    def set_data(self, data):
        self.__data = data

    def set_carrinho(self, carrinho):
        self.__carrinho = carrinho

    def set_total(self, total):
        self.__total = total

    def set_idCliente(self, cliente):
        self.__idCliente = cliente.get_id()

    def __str__(self):
        return f"Venda [ID: {self.__id}, Data: {self.__data}, Total: {self.__total}, Cliente ID: {self.__idCliente}]"

class VendaItem:

    def __init__(self, id, q, p):
        self._id = id
        self._qtd = q
        self._preco = p
        self._idVenda = Venda.get_id()
        self._idProduto = Produto.get_id() 
    
    def get_id(self):
        return self.__id

    def get_qtd(self):
        return self.__qtd

    def get_preco(self):
        return self.__preco

    def get_idVenda(self):
        return self.__idVenda
    
    def set_qtd(self, qtd):
        self.__qtd = qtd

    def set_preco(self, preco):
        self.__preco = preco

    def set_idVenda(self, venda):
        self.__idVenda = venda.get_id()

    def __str__(self):
        return f"VendaItem [ID: {self.__id}, Qtd: {self.__qtd}, Preço: {self.__preco}, ID Venda: {self.__idVenda}]"



class Produto:
    
    def __init__(self, id, d, p, e):
        self._id = id



class UI:
    @staticmethod
    def menu():
        print("Clientes")
        print("  1-Inserir, 2-Listar, 3-Atualizar, 4-Excluir, 9-Fim")
        return int(input("Escolha uma opção: "))
    @staticmethod
    def main():
        op = 0
        while op != 9:
            op = UI.menu()
            if op == 1: UI.cliente_inserir()
            if op == 2: UI.cliente_listar()
            if op == 3: UI.cliente_atualizar()
            if op == 4: UI.cliente_excluir()
    @staticmethod
    def cliente_inserir():
        id = int(input("Informe a numeração ID do cliente: "))
        nome = input("Informe o nome: ")
        email = input("Informe o e-mail: ")
        fone = input("Informe o fone: ")
        a = Cliente(id, nome, email, fone)
        Clientes.inserir(a)
    @staticmethod
    def cliente_listar():
        for cliente in Clientes.listar(): 
            print(cliente)
    @staticmethod
    def cliente_atualizar():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        email = input("Informe o novo e-mail: ")
        fone = input("Informe o novo fone: ")
        a = Cliente(id, nome, email, fone)
        Clientes.atualizar(a)
    @staticmethod
    def cliente_excluir():
        UI.cliente_listar()
        id = int(input("Informe o id do cliente a ser excluído: "))
        a = Cliente(id, "", "", "")
        Clientes.excluir(a)

UI.main()