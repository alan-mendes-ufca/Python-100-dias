"""Um galo custa 5, uma galinha custa 3 e três pintinhos custam 1.
Encontre todas as maneiras de comprar 100 galinhas com 100 moedas."""
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z % 3 == 0 and 5 * x + 3 * y + z // 3 == 100:
            print(x, y, z)
