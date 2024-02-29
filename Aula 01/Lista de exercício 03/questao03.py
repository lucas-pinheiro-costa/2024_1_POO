'''
3. Calcular a média parcial (ponderada) de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres
(pesos 2 e 3). Considerar as notas com valores inteiros entre zero e cem.
Digite a nota do primeiro bimestre da disciplina:   Exemplo:
50
Digite a nota do segundo bimestre da disciplina:
70
Média parcial = 62
'''

n1 = int(input('Digite a nota [0~100] do primeiro bimestre: '))
n2 = int(input('Digite a nota [0~100] do segundo bimestre: '))
media = ((n1*2)+(n2*3))/5
print('Media parcial = %d' % media)