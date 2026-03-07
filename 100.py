def sorteia():
    from random import randint
    cont = 0
    numeros = []
    par = 0
    while cont < 5:
        num = randint(1, 100)
        numeros.append(num)
        cont += 1
    print(f'Sorteando 5 valores da lista: ', end='')
    for valor in numeros:
        print(valor, end=' ')
        if valor % 2 == 0:
            par += 1
    if par == 1:
        print(f'\nHá {par} número par.')
    else:
        print(f'\nHá {par} números pares.')


sorteia()
