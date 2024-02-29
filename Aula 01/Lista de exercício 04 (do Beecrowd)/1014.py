'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total
de combustível gasto (em litros).

Entrada
O arquivo de entrada contém dois valores: um valor inteiro X representando a distância total
percorrida (em Km), e um valor real Y representando o total de combustível gasto, com um dígito
após o ponto decimal.

Saída
Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula,
seguido da mensagem "km/l".
'''

distancia = int(input('Informe a distancia total percorrida em Km: '))
combustivel = float(input('Informe a quantidade de combustivel gasto em litros: '))
consumo = distancia/combustivel

print(f'{consumo:.3f} km/l')