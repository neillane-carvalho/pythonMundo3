contagem = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = input('Digite um número entre 0 e 20 (ou "sair" para encerrar): ')

    if num.lower().strip() == 'sair':
        print('Encerrando o programa...')
        break

    try:
        num = int(num)
        if 0 <= num <= 20:
            print(f'O número digitado foi {contagem[num]}')
        else:
            print('Número fora do intervalo. Tente novamente.')
    except ValueError:
        print('Entrada inválida. Digite um número entre 0 e 20 ou "sair".')
