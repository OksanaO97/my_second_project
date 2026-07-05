print('Hello World')
print(5 + 4)
print(int('0101011', 2))
print('Введите целое положительное число для перевода его из десятичной в двоичную систему счисления')
num = int(input())
digit = ''
while num != 0:
    digit += str(num % 2)
    num =  num // 2
print(digit[::-1])