# Perguntar qual o número para calcular o fatorial
# Perguntar se deseja mostrar o calculo
# Se sim: mostrar o calculo
# Mostrar o fatorial do número
num = int(input('Digite um número para ver o fatorial: '))
num2 = num
while num != 1:
    print(num, 'x', end=' ')
    num = num - 1
else:
    print(num, '=')
