lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche[1])
for cont, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {cont}')
print(f'Comi pra caramba! Comi {len(lanche)} coisas!')
print(sorted(lanche))

a = ('1', '2', '3')
b = ('4', '5', '6', '5')
c = a + b
print(c)
c = b + a
print(c)
print(c.count('5'))
print(len(c))
print(c.index('6'))
print(c.index('5'))
print(c.index('5', 2))

pessoa = ('Neillane', 21, 'F', 98.5)
print(pessoa)
del(pessoa)
print(pessoa)
