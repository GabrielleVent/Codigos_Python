def fatorial():
    num = int(input('Digite um número para ver o fatorial: '))
    fatorial = 1
    print(f'O fatorial de {num}! é:', end=' ')
    for c in range(num, 0, -1):
        fatorial = fatorial*c

    while num != 1:
        print(num, 'x', end=' ')
        num = num - 1
    else:
        print(num, '=', end=' ')
    print(fatorial)


fatorial()
