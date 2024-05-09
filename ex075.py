numbers = (int(input('Digite um numero: ')),
           int(input('Digite outro numero: ')),
           int(input('Digite mais um numero:')),
           int(input('Digite o ultimo numero: ')))
print(f'Os valores digitados foram: {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)} vezes')
if 3 in numbers:
    print(f'O valor 3 apareceu na {numbers.index(3) + 1} posição')
else:
    print('O valor 3 não foi digitado')
print(f'Os valores pares digitados foram:', end='')
for n in numbers:
    if n % 2 == 0:
        print(n, end=' ')