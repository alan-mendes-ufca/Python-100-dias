## Algoritmo Primer Série 2: Retrocesso e Recursão

Esta palestra continua a série de algoritmos com recursão e retrocesso.

### Recursão

Recursão significa definir ou resolver algo em termos de si mesmo.

Exemplos usados ​​na palestra:

- histórias autorreferenciais
- definição fatorial recursiva
- problema recursivo de contagem de escadas

Pontos importantes ao escrever funções recursivas:

1. caso base: quando a recursão para
2. relação de recorrência: como o estado atual depende dos estados anteriores

A palestra também observa que o Python limita a profundidade da recursão por padrão e mostra como ajustá-la com `sys.setrecursionlimit`.

### Retrocesso

Backtracking é uma forma estruturada de pesquisa de força bruta. Ele constrói soluções candidatas passo a passo e abandona ramificações assim que elas não conseguem mais levar a uma resposta válida.

Exemplos clássicos discutidos:

- resolução de labirinto
- passeio do cavaleiro
- oito rainhas

A principal lição é que a recursão é uma ferramenta útil, mas nem sempre a melhor. Se existir uma abordagem iterativa ou otimizada mais limpa, prefira isso em vez de usar a recursão por hábito.
