'''
Calcular área, perímetro e diagonal de um retângulo, dados sua base e sua altura. Considerar que os valores
podem ser números reais. Mostrar o resultado com duas casas decimais.
Digite a base e a altura do retângulo
3
4
Área = 12.00 - Perímetro = 14.00 - Diagonal = 5.00
'''

base, altura = map(float, input('Digite a base e a altura do retangulo: ').split())
area = base * altura
perimetro = (base + altura) * 2
diagonal = ((base * base) + (altura * altura)) ** (1/2)

print(f'Area = {area:.2f} - Perimetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}')