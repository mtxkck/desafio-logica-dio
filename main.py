def ranque(xp):
    if xp <= 1000:
        return "ferro"
    elif xp <= 1001:
        return "Bronze"
    elif xp <= 2001:
        return "Prata"
    elif xp <= 6001:
        return "Ouro"
    elif xp <= 7001:
        return "Platina"
    elif xp <= 8001:
        return "Ascendente"
    elif xp <= 9001:
        return "Imortal"
    else:
        return "Radiante"

nome = input("Digite o nome do seu heroi: ")
xp = int(input(f"Digite o xp do seu heroi ({nome}): "))
print(f"O Heroi de nome {nome} esta no nivel de {ranque(xp)}!")