## Um pequeno exemplo para realmente compreender as corrotinas

Esta nota usa um exemplo mínimo para explicar corrotinas intuitivamente.

O objetivo é mostrar:

- o que é uma corrotina
- como o controle é obtido
- como múltiplas tarefas cooperam sem threading tradicional

As corrotinas se tornam muito mais fáceis de entender quando você para de pensar nelas como "sintaxe assíncrona mágica" e começa a vê-las como suspensão controlada e retomada de execução.
