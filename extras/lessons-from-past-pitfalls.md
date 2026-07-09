## Armadilhas que encontramos ao longo dos anos

Esta nota coleta armadilhas sutis do Python que confundem facilmente os alunos.

### Armadilha 1: comparação de números inteiros

Explica a diferença entre:

- `==`: igualdade de valor
- `is`: comparação de identidade

Em seguida, ele usa o comportamento de cache de números inteiros pequenos do CPython para mostrar por que `is` pode produzir resultados surpreendentes com números inteiros.

### Armadilha 2: listas aninhadas

A nota também aborda a armadilha clássica de lista aninhada, em que listas internas repetidas podem se referir ao mesmo objeto, causando atualizações compartilhadas inesperadas.

A lição geral é que Python geralmente parece simples superficialmente, mas a identidade do objeto e as referências compartilhadas ainda são importantes.
