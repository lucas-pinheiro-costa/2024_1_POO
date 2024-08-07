'''
2. Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o
primeiro nome da pessoa.
Digite seu nome completo:
Gilbert Azevedo da Silva
Bem-vindo ao Python, Gilbert
'''

nome  = list(input('Digite seu nome completo: ').split())
print('Bem-vindo ao Python,', nome[0])