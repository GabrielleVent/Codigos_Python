from random import randint
lista = []
jogadores = {'jogador1': randint(1, 6), 'Jogador2': randint(
    1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in jogadores.items():
    lista.append(v)
    print(lista)
