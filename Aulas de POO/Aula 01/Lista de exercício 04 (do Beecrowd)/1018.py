'''
Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor 
pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido 
e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o 
exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa 
apresentará a mensagem: “Presentation Error”.
'''
numero = int(input())
valor = numero
cedulas100 = valor//100
valor = valor - (cedulas100*100)
cedulas50 = valor//50
valor = valor - (cedulas50*50)
cedulas20 = valor//20
valor = valor - (cedulas20*20)
cedulas10 = valor//10
valor = valor - (cedulas10*10)
cedulas5 = valor//5
valor = valor - (cedulas5*5)
cedulas2 = valor//2
cedulas1 = valor - (cedulas2*2)

print(f'{numero}\n')
print(f'{cedulas100} nota(s) de R$ 100,00\n')
print(f'{cedulas50} nota(s) de R$ 50,00\n')
print(f'{cedulas20} nota(s) de R$ 20,00\n')
print(f'{cedulas10} nota(s) de R$ 10,00\n')
print(f'{cedulas5} nota(s) de R$ 5,00\n')
print(f'{cedulas2} nota(s) de R$ 2,00\n')
print(f'{cedulas1} nota(s) de R$ 1,00\n')