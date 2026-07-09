## Use uma função ou uma expressão complexa?

Este ensaio explora uma questão comum de legibilidade: você deve agrupar a lógica em uma única expressão inteligente ou extrair uma função auxiliar?

Usando o exemplo "máximo de três números", mostra como o código pode evoluir a partir de:

- lógica multilinha explícita
- para expressões ternárias
- para one-liners excessivamente compactados
- para uma função auxiliar mais limpa

A lição principal é simples:

- mais curto nem sempre é mais claro
- funções auxiliares geralmente melhoram a legibilidade e a reutilização

O `max` integrado do Python resolve o exemplo diretamente, mas a lição de design mais ampla permanece útil.
