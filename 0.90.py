nota = {}
nota['nome'] = str(input('Nome: '))
nota['media'] = float(input('Média: '))
print(f'- O nome é igual a {nota["nome"]}!')
print(f'- A média é igual a {nota["media"]}')
if nota['media'] >= 7.0:
    print('- Situação: Aprovado!')
else:
    print('- Situação: Reprovado!')
