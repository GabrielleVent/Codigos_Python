# receber varios numeros inteiros
# analisar qual número é o maior

def maior(*num):
    maior_num = 0
    print(f'A sequência digitada foi: ', end='')
    for numero in num:
        print(numero, end=' ')
        if numero > maior_num:
            maior_num = numero
    print(f'\nO maior número é {maior_num}.')


maior(0, 8, 6, 200, 1, 151)
