## Python divertido

Esta nota de aula pública mostra maneiras divertidas e fáceis de explorar Python para iniciantes.

### Um shell interativo melhor

A palestra recomenda `ipython` porque oferece:

- `?` e `??` para obter ajuda
- `!` para comandos shell
- conclusão da guia
- comandos mágicos como `%timeit`

Instale-o com:

```bash
pip install ipython
```

### Processamento de imagem com travesseiro

A palestra usa Pillow para demonstrar operações divertidas de imagem, como:

- carregando uma imagem
- aplicando filtros
- recortar e colar
- espelhamento
- gerando miniaturas

Fluxo de trabalho típico de travesseiro:

```python
from PIL import Image, ImageFilter
```

O ponto principal é que o Python pode ser usado não apenas para back-end sério ou trabalho de dados, mas também para pequenos experimentos visuais e criativos que tornam o aprendizado mais agradável.
