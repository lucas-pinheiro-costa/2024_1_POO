# Função para verificar se um número é primo
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Lendo o número de casos de teste
N = int(input())

# Verificando cada caso de teste
for _ in range(N):
    X = int(input())
    if is_prime(X):
        print("Prime")
    else:
        print("Not Prime")