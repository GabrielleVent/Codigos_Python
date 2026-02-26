def voto(ano=0):
    ano = int(input('Em que ano você nasceu? '))
    if 2025-ano >= 16 and 2025-ano < 18:
        print(f'Seu voto é facultativo! Você tem {2025-ano} anos.')
    if 2025-ano >= 18:
        print(f'Você tem {2025-ano} anos. Você pode votar!')
    if 2025-ano < 16:
        print(f'Você tem {2025-ano}. Você não pode votar ainda!')


voto()
