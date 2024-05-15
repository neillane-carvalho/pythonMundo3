lista = [5,2,4,3,1]
print(lista)
lista[1] = 6
print(lista)
lista.append(7)
print(lista)
lista.sort()
print(lista)
lista.reverse()
print(lista)
print(f'Essa lista tem {len(lista)} elementos')
lista.insert(2, 0)
print(lista)
if 5 in lista:
    lista.remove(5)
    print(lista)
else:
    print('O valor 5 não foi encontrado na lista')
print(f'Essa lista tem {len(lista)} elementos')
