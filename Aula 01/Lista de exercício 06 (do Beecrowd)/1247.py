import math

def pode_interceptar(D, VF, VG):
    # Calcula o tempo que a Guarda Costeira e o fugitivo levam para alcançar as 12 milhas
    tempo_guarda = 12 / VG
    tempo_fugitivo = D / VF
    
    # Verifica se a Guarda Costeira pode interceptar o fugitivo antes das 12 milhas
    if tempo_guarda >= tempo_fugitivo:
        return 'S'
    else:
        return 'N'

# Processa os casos de teste
while True:
    try:
        # Lê os valores de D, VF e VG
        D, VF, VG = map(int, input().split())
        
        # Verifica se a Guarda Costeira pode interceptar o fugitivo
        resultado = pode_interceptar(D, VF, VG)
        print(resultado)
        
    except EOFError:
        break  # Encerra o loop quando atingir o final do arquivo de entrada