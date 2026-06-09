vendas = [3, 5, 2, 8, 1, 4]
quant_vendas = 0
tot = 0
maior_venda = 0
menor_venda = vendas[0]
for venda in vendas:
    quant_vendas = quant_vendas+1
    tot = tot + venda
    if venda > maior_venda:
        maior_venda = venda
    if venda < menor_venda:
        menor_venda = venda
media = tot/quant_vendas
print(
    f'''Quantidade de vendas: {quant_vendas}\nTotal vendido: {tot}\nMaior venda: {maior_venda}\nMenor venda: {menor_venda}\nMédia: {media:.2f}''')
