num1, num2, num3 = map(int, input().split())
maior1 = (num1+num2+abs(num1-num2))//2
maior2 = (maior1+num3+abs(maior1-num3))//2

print(f'{maior2} eh o maior')
