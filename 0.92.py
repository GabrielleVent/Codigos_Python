from datetime import date
pessoas = {'nome': str(input('Nome: ')), 'idade': date.today(
).year - int(input('Ano do nascimento: ')), 'CTPS': int(input('CTPS (0 não tem): '))}
if pessoas['CTPS'] != 0:
    pessoas['contratação'] = int(input('Ano de contratação: '))
    pessoas['salário'] = int(input('Salário R$: '))
print('=*'*10)
for v, k in pessoas.items():
    print(f'- {v} tem valor {k}')
