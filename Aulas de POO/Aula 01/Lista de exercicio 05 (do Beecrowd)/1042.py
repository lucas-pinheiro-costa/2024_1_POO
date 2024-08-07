'''
Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, 
uma linha em branco e em seguida, os valores na sequência como foram lidos.

Entrada
A entrada contem três números inteiros.

Saída
Imprima a saída conforme foi especificado.
'''

num = list(map(int, input().split()))
ordenado = num.copy()
ordenado.sort()

print(ordenado[0])
print(ordenado[1])
print(ordenado[2])
print('\n')
print(num[0])
print(num[1])
print(num[2])