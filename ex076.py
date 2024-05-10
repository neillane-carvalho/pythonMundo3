listagem = ('Lápis', 1.75,
            'caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 2.70,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 54)
print('_'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('_'*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>4.2f}')
print('_'*40)