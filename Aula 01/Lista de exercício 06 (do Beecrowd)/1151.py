'''
A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. 
Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. 
Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 46).

Saída
Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. 
Não deve haver espaço após o último valor.
'''

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Lendo o valor de N
N = int(input())

# Imprimindo os N primeiros números da série de Fibonacci
for i in range(1, N+1):
    # Se i for igual a N-1 (o último número na sequência), não adicionar espaço extra
    if i == N:
        print(fibonacci(i-1), end="")
    else:
        print(fibonacci(i-1), end=" ")

# ERA PRA FUNCIONAR MAS O BEECROWD TÁ DE SACANAGEM
