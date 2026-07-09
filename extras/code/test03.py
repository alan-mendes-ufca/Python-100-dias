from random import randint, sample

# Construa o conjunto de bolas vermelhas.
red_balls = [x for x in range(1, 34)]
# Selecione seis bolas vermelhas.
selected_balls = sample(red_balls, 6)
# Classifique as bolas vermelhas.
selected_balls.sort()
# Adicione uma bola azul.
selected_balls.append(randint(1, 16))
# Imprima os números gerados.
for index, ball in enumerate(selected_balls):
    print('%02d' % ball, end=' ')
    if index == len(selected_balls) - 2:
        print('|', end=' ')
print()
