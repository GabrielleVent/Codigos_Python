num = int(input('Digite o número para ver o fatorial: '))
fatorial = 1
for c in range(num, 0, -1):
    fatorial = fatorial*c
print(f'O fatorial de {num} é {fatorial}.')
