# nome do jogador e o número de gols q ele fez
# devo imprimir na tela
# o programa devera mostrar a ficha, mesmo sem algum dos dados
# o programa deve mostrar o nome do jogador e quantos gols ele fez
# Sequencia de passos:
# perguntar o nome do jogador
# perguntar quantos gols o jogador fez
# mostrar o nome do jogador e a quantidade de gols feita
def ficha(nome='', gols=''):
    nome = str(input('Nome: '))
    gols = str(input('Gols: '))
    if nome == '' or nome.isalpha() == False:
        nome = '<<desconhecido>>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s)!')


ficha()
