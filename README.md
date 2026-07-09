## Python – 100 dias do iniciante ao mestre

---
> Tradução não oficial para português do projeto Python-100-Days.
> Conteúdo original criado por [Luo Hao / jackfrued](https://github.com/jackfrued/Python-100-Days).
> Esta versão tem finalidade de estudo e adaptação linguística. Consulte [NOTICE.md](./NOTICE.md) antes de redistribuir o material.
---

### Pré-requisitos

- Python 3.12 é o ambiente de referência, com `pip` disponível no terminal.
- Crie um ambiente virtual antes de instalar bibliotecas de terceiros:

  ```bash
  python -m venv .venv
  source .venv/bin/activate  # Windows PowerShell: .venv\Scripts\Activate.ps1
  python -m pip install --upgrade pip
  ```

- As dependências estão separadas por trilha em `requirements/`. Use `basics.txt`, `documents.txt` e `media.txt` nos dias 1 a 30; `advanced-python.txt` nos dias 31 a 35; `database.txt` nos dias 36 a 45; `web.txt` nos dias 46 a 60; `scraping.txt` nos dias 61 a 65; e `data.txt` nos dias 66 a 90. `requirements/all.txt` reúne as trilhas principais. Exercícios especializados mantêm instruções próprias em sua aula.

### Áreas de aplicação Python e análise de desenvolvimento de carreira

Simplificando, Python é uma linguagem de programação “elegante”, “explícita” e “simples”.

- A curva de aprendizado é baixa e até mesmo quem não é profissional pode começar.
- É um sistema de código aberto e possui um ecossistema poderoso.
- É uma linguagem interpretada com perfeita portabilidade de plataforma.
- É uma linguagem de tipo dinâmico que suporta programação orientada a objetos e funcional.
- Seu estilo de código é altamente padronizado e muito legível.

Python pode mostrar sua habilidade nos seguintes campos.

- Desenvolvimento back-end - Python/Java/Go/PHP
- DevOps - Python/Shell/Ruby
- Coleta de dados - Python/C++/Java
- Negociação quantitativa - Python / C++ / R
- Ciência de dados - Python / R / Julia / Matlab
- Aprendizado de máquina - Python / R / C++ / Julia
- Testes automatizados – Python/Shell

Como desenvolvedor Python, de acordo com suas preferências pessoais e planejamento de carreira, também existem muitos campos de trabalho à sua escolha.

- Engenheiro de back-end Python (servidores, plataformas em nuvem, APIs de dados)
- Engenheiro de operações Python (operações automatizadas, SRE, DevOps)
- Analista de dados Python (análise de dados, business intelligence, operações digitais)
- Cientista de dados Python (aprendizado de máquina, aprendizado profundo, especialista em algoritmos)
- Engenheiro rastreador Python (esta faixa não é recomendada!!!)
- Engenheiro de testes Python (testes automatizados, desenvolvimento de testes)

> **Observação**: Atualmente, o **caminho da ciência de dados é uma direção muito quente**, porque não importa se é a indústria da Internet ou as indústrias tradicionais, elas já acumularam uma grande quantidade de dados. Todas as esferas da vida precisam que os cientistas de dados descubram mais valor comercial a partir dos dados existentes, de modo a fornecer suporte de dados para decisões empresariais. Isso é o que chamamos de tomada de decisão baseada em dados.

Várias sugestões para iniciantes:

- **Faça do inglês seu idioma de trabalho.**
- **A prática leva à perfeição.**
- **Toda experiência vem dos erros que você cometeu.**
- **Não seja um aproveitador.**
- **Adote a IA para aumentar sua produtividade.**

### Dia 01~20 - Noções básicas da linguagem Python

#### Dia 01 - [Introdução ao Python](./Day01-20/01.getting-started-with-python.md)

1. Introdução ao Python
   - Uma breve história do Python
   - Prós e contras do Python
   - Áreas de aplicação Python
2. Instalando o ambiente Python
   - Ambiente Windows
   - ambiente macOS

#### Dia 02 - [O primeiro programa Python](./Day01-20/02.first-python-program.md)

1. Ferramentas para escrever código
2. Olá, mundo
3. Comentando seu código

#### Dia 03 - [Variáveis em Python](./Day01-20/03.variables-in-python.md)

1. Algum bom senso básico
2. Variáveis e tipos
3. Nomenclatura de variáveis
4. Usando variáveis

#### Dia 04 - [Operadores em Python](./Day01-20/04.operators-in-python.md)

1. Operadores aritméticos
2. Operadores de atribuição
3. Operadores de comparação e operadores lógicos
4. Aplicações de operadores e expressões
   - Conversão Fahrenheit e Celsius
   - Calculando a circunferência e a área de um círculo
   - Determinar se um ano é bissexto

#### Dia 05 - [Ramificação](./Day01-20/05.branching.md)

1. Construindo estruturas ramificadas com `if` e `else`
2. Construindo estruturas ramificadas com `match` e `case`
3. Aplicações de estruturas ramificadas
   - Avaliando uma função por partes
   - Convertendo notas percentuais em níveis de notas
   - Calculando o perímetro e a área de um triângulo

#### Dia 06 - [Laços](./Day01-20/06.loops.md)

1. Laços `for-in`
2. Laços `while`
3. `break` e `continue`
4. Estruturas de laços aninhadas
5. Aplicações de laços
   - Determinando números primos
   - Maior divisor comum
   - Jogo de adivinhar o número

#### Dia 07 - [Estruturas condicionais e laços na prática](./Day01-20/07.branching-and-loops-in-practice.md)

1. Exemplo 1: números primos dentro de 100
2. Exemplo 2: sequência de Fibonacci
3. Exemplo 3: Encontrando números narcisistas
4. Exemplo 4: O problema das cem galinhas
5. Exemplo 5: O jogo de azar CRAPS

#### Dia 08 - [Estrutura de dados comum: lista - 1](./Day01-20/08.lists-1.md)

1. Criando listas
2. Listar operações
3. Percorrendo elementos

#### Dia 09 - [Estrutura de dados comum: lista - 2](./Day01-20/09.lists-2.md)

1. Listar métodos
   - Adicionando e excluindo elementos
   - Posições e frequências dos elementos
   - Classificando e revertendo elementos
2. Compreensões de lista
3. Listas aninhadas
4. Aplicações de listas

#### Dia 10 - [Estrutura de dados comum: tupla](./Day01-20/10.tuples.md)

1. Definição e operações de tupla
2. Empacotar e desembalar
3. Trocando valores de variáveis
4. Comparando tuplas e listas

#### Dia 11 - [Estrutura de dados comum: String](./Day01-20/11.strings.md)

1. Definindo cadeias de caracteres
   - Caracteres de escape
   - Strings brutas
   - Representações de caracteres especiais
2. Operações de string
   - Concatenação e repetição
   - Operações de comparação
   - Operações de pertinência
   - Obtendo o comprimento da string
   - Indexação e fatiamento
3. Iterando sobre caracteres
4. Métodos de string
   - Conversão de caso
   - Operações de pesquisa
   - Verificações de propriedade
   - Formatação
   - Aparar
   - Substituindo
   - Dividir e juntar
   - Codificação e decodificação
   - Outros métodos

#### Dia 12 - [Estrutura de dados comum: conjunto](./Day01-20/12.sets.md)

1. Criando conjuntos
2. Variáveis de elementos
3. Definir operações
   - Operações de pertinência
   - Operações binárias
   - Operações de comparação
4. Definir métodos
5. Conjuntos imutáveis

#### Dia 13 - [Estrutura de dados comum: dicionário](./Day01-20/13.dictionaries.md)

1. Criando e usando dicionários
2. Operações de dicionário
3. Métodos de dicionário
4. Aplicações de dicionários

#### Dia 14 - [Funções e Módulos](./Day01-20/14.functions-and-modules.md)

1. Definindo funções
2. Parâmetros de função
   - Argumentos posicionais e argumentos de palavras-chave
   - Valores padrão para argumentos
   - Argumentos de comprimento variável
3. Gerenciando funções com módulos
4. Módulos e funções na biblioteca padrão

#### Dia 15 - [Prática de Função](./Day01-20/15.function-practice.md)

1. Exemplo 1: código de verificação aleatório
2. Exemplo 2: Determinando números primos
3. Exemplo 3: Máximo divisor comum e mínimo múltiplo comum
4. Exemplo 4: estatísticas de dados
5. Exemplo 5: Seleção aleatória de número de bola de duas cores

#### Dia 16 - [Uso de função avançada](./Day01-20/16.advanced-functions.md)

1. Funções de ordem superior
2. Funções lambda
3. Funções parciais

#### Dia 17 - [Aplicativos de funções avançadas](./Day01-20/17.advanced-function-applications.md)

1. Decoradores
2. Chamadas recursivas

#### Dia 18 - [Introdução à Programação Orientada a Objetos](./Day01-20/18.object-oriented-programming-intro.md)

1. Classes e objetos
2. Definindo classes
3. Criando e usando objetos
4. Métodos de inicialização
5. Os pilares da orientação a objetos
6. Casos orientados a objetos
   - Exemplo 1: Um relógio digital
   - Exemplo 2: Um ponto em um plano

#### Dia 19 - [Programação Avançada Orientada a Objetos](./Day01-20/19.object-oriented-programming-advanced.md)

1. Visibilidade e decoradores de propriedades
2. Atributos dinâmicos
3. Métodos estáticos e métodos de classe
4. Herança e polimorfismo

#### Dia 20 - [Programação Orientada a Objetos na Prática](./Day01-20/20.object-oriented-programming-in-practice.md)

1. Jogo de pôquer
2. Sistema de liquidação de folha de pagamento

### Dia 21~30 - Aplicações em linguagem Python

#### Dia 21 - [E/S de arquivos e tratamento de exceções](./Day21-30/21.file-io-and-exception-handling.md)

1. Abrindo e fechando arquivos
2. Lendo e escrevendo arquivos de texto
3. Mecanismos de tratamento de exceções
4. Sintaxe do gerenciador de contexto
5. Lendo e gravando arquivos binários

#### Dia 22 - [Serialização e desserialização de objetos](./Day21-30/22.serialization-and-deserialization.md)

1. Visão geral do JSON
2. Lendo e gravando dados JSON
3. A ferramenta de gerenciamento de pacotes `pip`
4. Obtendo dados por meio de APIs da web

#### Dia 23 - [Lendo e gravando arquivos CSV com Python](./Day21-30/23.working-with-csv-files.md)

1. Introdução aos arquivos CSV
2. Gravando dados em arquivos CSV
3. Lendo dados de arquivos CSV

#### Dia 24 - [Lendo e escrevendo arquivos Excel com Python - 1](./Day21-30/24.working-with-excel-files-1.md)

1. Introdução ao Excel
2. Lendo arquivos Excel
3. Escrevendo arquivos Excel
4. Ajustando estilos
5. Cálculo de fórmula

#### Dia 25 - [Lendo e gravando arquivos Excel com Python - 2](./Day21-30/25.working-with-excel-files-2.md)

1. Introdução ao Excel
2. Lendo arquivos Excel
3. Escrevendo arquivos Excel
4. Ajustando estilos
5. Gerando gráficos estatísticos

#### Dia 26 - [Trabalhando com arquivos Word e PowerPoint em Python](./Day21-30/26.working-with-word-and-powerpoint.md)

1. Trabalhando com documentos do Word
2. Gerando apresentações em PowerPoint

#### Dia 27 - [Trabalhando com arquivos PDF em Python](./Day21-30/27.working-with-pdf-files.md)

1. Extraindo texto de arquivos PDF
2. Girar e sobrepor páginas
3. Criptografando arquivos PDF
4. Marca d'água em lote
5. Criando arquivos PDF

#### Dia 28 - [Processamento de imagem com Python](./Day21-30/28.image-processing.md)

1. Conceitos introdutórios
2. Processando imagens com Pillow
3. Desenhando com Pillow

#### Dia 29 - [Envio de e-mail e SMS com Python](./Day21-30/29.sending-email-and-sms.md)

1. Enviando e-mail
2. Envio de mensagens de texto

#### Dia 30 - [Aplicações de Expressões Regulares](./Day21-30/30.regular-expressions-in-practice.md)

1. Conhecimento relacionado a expressões regulares
2. Suporte Python para expressões regulares
   - Exemplo 1: validação de entrada
   - Exemplo 2: Extração de conteúdo
   - Exemplo 3: Substituição de conteúdo
   - Exemplo 4: divisão de frases longas

### Dia 31~35 - Outros conteúdos relacionados

#### [Python avançado](./Day31-35/31.python-advanced.md)

1. Pontos de conhecimento importantes
2. Estruturas de dados e algoritmos
3. Maneiras de usar funções
4. Conhecimento orientado a objetos
5. Iteradores e geradores
6. Programação simultânea

#### [Introdução ao front-end da Web](./Day31-35/32-33.web-frontend-introduction.md)

1. Usando tags HTML para transportar o conteúdo da página
2. Renderizando páginas com CSS
3. Lidando com comportamento interativo com JavaScript
4. Introdução ao Vue.js
5. Usando Elemento
6. Usando Bootstrap

#### [Brincando com o sistema operacional Linux](./Day31-35/34-35.linux-basics.md)

1. História do desenvolvimento de sistemas operacionais e uma visão geral do Linux
2. Comandos básicos do Linux
3. Utilitários no Linux
4. O sistema de arquivos Linux
5. Aplicações do editor Vim
6. Variáveis de ambiente e programação shell
7. Instalação de software e configuração de serviço
8. Acesso e gerenciamento de rede
9. Outros conteúdos relacionados

### Dia 36~45 - Noções básicas de banco de dados e tópicos avançados

#### Dia 36 - [Visão geral de bancos de dados relacionais e MySQL](./Day36-45/36.relational-databases-and-mysql-overview.md)

1. Visão geral dos bancos de dados relacionais
2. Introdução ao MySQL
3. Instalando MySQL
4. Comandos básicos do MySQL

#### Dia 37 - [SQL em detalhes: DDL](./Day36-45/37.sql-ddl.md)

1. Criação de bancos de dados e tabelas
2. Eliminando tabelas e modificando tabelas

#### Dia 38 - [SQL em detalhes: DML](./Day36-45/38.sql-dml.md)

1. Operações `insert`
2. Operações `delete`
3. Operações `update`

#### Dia 39 - [SQL em detalhes: DQL](./Day36-45/39.sql-dql.md)

1. Projeção e aliases
2. Filtrando dados
3. Tratamento nulo
4. Desduplicação
5. Classificando
6. Funções agregadas
7. Consultas aninhadas
8. Agrupamento
9. Junções de tabela
   - Produto cartesiano
   - Junção interna
   - Junção natural
   - Junção externa
10. Funções de janela
   - Definindo janelas
   - Funções de classificação
   - Funções de recuperação de valor

#### Dia 40 - [SQL em detalhes: DCL](./Day36-45/40.sql-dcl.md)

1. Criando usuários
2. Concessão de privilégios
3. Revogando privilégios

#### Dia 41 - [Novos recursos do MySQL](./Day36-45/41.mysql-new-features.md)

- Tipo JSON
- Funções de janela
- Expressões de tabela comuns

#### Dia 42 - [Visualizações, funções e procedimentos](./Day36-45/42.views-functions-and-procedures.md)

1. Visualizações
   - Cenários de uso
   - Criando visualizações
   - Restrições de uso
2. Funções
   - Funções integradas
   - Funções definidas pelo usuário (UDF)
3. Procedimentos
   - Criando procedimentos
   - Procedimentos de chamada

#### Dia 43 - [Índices](./Day36-45/43.indexes.md)

1. Planos de execução
2. Princípios de indexação
3. Criando índices
   - Índices regulares
   - Índices exclusivos
   - Índices de prefixo
   - Índices compostos
4. Pontos a serem observados

#### Dia 44 - [Python conectando-se a um banco de dados MySQL](./Day36-45/44.python-and-mysql.md)

1. Instalando bibliotecas de terceiros
2. Criando uma conexão
3. Obtendo um cursor
4. Executando instruções SQL
5. Buscando dados através de um cursor
6. Confirmação e reversão de transação
7. Liberando conexões
8. Escrevendo scripts ETL

#### Dia 45 - [Hive na prática](./Day36-45/45.hive-in-practice.md)

1. Visão geral do Hive
2. Configuração do ambiente
3. Comandos comuns
4. Sintaxe básica
5. Operações de criação de tabela
6. Gravando dados
7. Funções comuns
8. Agrupamento e agregação
9. Operações de amostragem
10. Operações de classificação
11. Expansão lateral
12. Otimização de desempenho

### Dia 46~60 - Django na Prática

#### Dia 46 - [Começando com Django rapidamente](./Day46-60/46.getting-started-with-django.md)

1. Como funcionam os aplicativos da web
2. Solicitações e respostas HTTP
3. Visão geral da estrutura Django
4. Um início rápido em 5 minutos

#### Dia 47 - [Modelos em profundidade](./Day46-60/47.models-in-depth.md)

1. Configuração do banco de dados relacional
2. Usando o ORM para concluir operações CRUD em modelos
3. Usando o back-end do administrador
4. Melhores práticas do modelo Django
5. Referência de definição de modelo

#### Dia 48 - [Recursos estáticos e solicitações Ajax](./Day46-60/48.static-assets-and-ajax.md)

1. Carregando recursos estáticos
2. Visão geral do Ajax
3. Usando Ajax para implementar votação

#### Dia 49 - [Cookie e Sessão](./Day46-60/49.cookies-and-sessions.md)

1. Implementando rastreamento de usuários
2. A relação entre cookies e sessões
3. Suporte ao framework Django para sessões
4. Ler e escrever cookies nas funções de visualização

#### Dia 50 - [Relatórios e registros](./Day46-60/50.reporting.md)

1. Modificando cabeçalhos de resposta por meio de `HttpResponse`
2. Usando `StreamingHttpResponse` para lidar com arquivos grandes
3. Usando `xlwt` para gerar relatórios Excel
4. Usando `reportlab` para gerar relatórios em PDF
5. Usando ECharts para gerar gráficos frontend

#### Dia 51 - [Logs e a barra de ferramentas de depuração](./Day46-60/51.logging-and-debug-toolbar.md)

1. Configurando registros
2. Configurando a barra de ferramentas de depuração do Django
3. Otimizando o código ORM

#### Dia 52 - [Aplicações de Middleware](./Day46-60/52.middleware.md)

1. O que é middleware
2. Middleware integrado no Django
3. Middleware customizado e seus cenários de aplicação

#### Dia 53 - [Introdução ao desenvolvimento de separação frontend-backend](./Day46-60/53.frontend-backend-separation-intro.md)

1. Retornando dados no formato JSON
2. Renderizando páginas com Vue.js

#### Dia 54 - [Arquitetura RESTful e noções básicas de DRF](./Day46-60/54.restful-architecture-and-drf-intro.md)

1. Visão geral do REST
2. Introdução à biblioteca DRF
3. Desenvolvimento de separação frontend-backend
4. Aplicações de JWT

#### Dia 55 - [Arquitetura RESTful e DRF Avançado](./Day46-60/55.restful-architecture-and-drf-advanced.md)

1. Usando CBV
2. Paginação de dados
3. Filtragem de dados

#### Dia 56 - [Usando cache](./Day46-60/56.caching.md)

1. A primeira lei da otimização de sites
2. Usando Redis para fornecer serviços de cache em projetos Django
3. Lendo e gravando cache em funções de visualização
4. Usando decoradores para implementar cache de página
5. Fornecimento de serviços de cache para APIs de dados

#### Dia 57 - [Conectando plataformas de terceiros](./Day46-60/57.third-party-platform-integration.md)

1. Controles de formulário de upload de arquivos e visualização de imagens
2. Como o servidor lida com os arquivos carregados

#### Dia 58 - [Tarefas Assíncronas e Tarefas Agendadas](./Day46-60/58.async-and-scheduled-tasks.md)

1. A segunda lei da otimização de sites
2. Configurando um serviço de fila de mensagens
3. Usando o Celery em um projeto para tornar as tarefas assíncronas
4. Usando o Celery em um projeto para implementar tarefas agendadas

#### Dia 59 - [Estratégia de testes: TDD, testes unitários e integração](./Day46-60/59.unit-testing.md)

1. Pirâmide de testes e seleção do nível adequado
2. Desenvolvimento orientado a testes (TDD)
3. Testes unitários, de integração e ponta a ponta
4. Mocks, cobertura e integração contínua

#### Dia 60 - [Projeto ficando on-line](./Day46-60/60.project-deployment.md)

1. Usando sistemas de controle de versão
2. Configurando e usando uWSGI
3. Separando recursos dinâmicos e estáticos e configurando o Nginx
4. Configurando HTTPS
5. Configurando a resolução de nomes de domínio

### Dia 61~65 - Coleta de dados da Web

#### Dia 61 - [Visão geral da coleta de dados da Web](./Day61-65/61.web-data-collection-overview.md)

1. O conceito de web crawlers e suas áreas de aplicação
2. Discussão sobre a legalidade dos rastreadores da web
3. Ferramentas relacionadas ao desenvolvimento de rastreadores da web
4. A estrutura de um programa rastreador

#### Dia 62 - Busca e análise de dados

1. [Usando a biblioteca de terceiros `requests` para buscar dados](./Day61-65/62.fetching-web-resources.md)
2. [Três maneiras de analisar páginas](./Day61-65/62.parsing-html-with-python.md)
   - Análise de expressão regular
   - Análise XPath
   - Análise do seletor CSS

#### Dia 63 - Programação Simultânea em Python

1. [Multithreading](./Day61-65/63.concurrent-programming-in-python-1.md)
2. [Multiprocessamento](./Day61-65/63.concurrent-programming-in-python-2.md)
3. [E/S assíncrona](./Day61-65/63.concurrent-programming-in-python-3.md)

#### Dia 64 - [Usando Selenium para buscar conteúdo dinâmico da Web](./Day61-65/64.selenium-for-dynamic-content.md)

1. Instalando Selenium
2. Carregando páginas
3. Encontrar elementos e simular o comportamento do usuário
4. Esperas implícitas e esperas explícitas
5. Executando código JavaScript
6. Quebrando as proteções anti-crawler com Selenium
7. Configurando um navegador sem cabeça

#### Dia 65 - [Introdução à estrutura do Scrapy Crawler](./Day61-65/65.introduction-to-scrapy.md)

1. Componentes principais do Scrapy
2. O fluxo de trabalho Scrapy
3. Instalando Scrapy e criando um projeto
4. Escrevendo programas spider
5. Escrevendo programas de middleware e pipeline
6. Arquivos de configuração raspados

### Dia 66 ~ 80 - Análise de dados Python

#### Dia 66 - [Visão geral da análise de dados](./Day66-80/66.data-analysis-overview.md)

1. Responsabilidades de um analista de dados
2. A pilha de habilidades de um analista de dados
3. Bibliotecas de análise de dados

#### Dia 67 - [Preparação do Ambiente](./Day66-80/67.environment-setup.md)

1. Instalando e usando o Anaconda
   - Comandos relacionados a `conda`
2. Instalando e usando JupyterLab
   - Instalação e inicialização
   - Dicas úteis

#### Dia 68 - [Aplicações de NumPy - 1](./Day66-80/68.numpy-applications-1.md)

1. Criando objetos de array
2. Propriedades de objetos array
3. Operações de indexação em objetos array
   - Indexação regular
   - Indexação sofisticada
   - Indexação booleana
   - Indexação de fatia
4. Estudo de caso: usando arrays para processar imagens

#### Dia 69 - [Aplicações de NumPy - 2](./Day66-80/69.numpy-applications-2.md)

1. Métodos relacionados a objetos array
   - Obtenção de estatísticas descritivas
   - Outros métodos relacionados

#### Dia 70 - [Aplicações de NumPy - 3](./Day66-80/70.numpy-applications-3.md)

1. Operações de matriz
   - Operações entre arrays e escalares
   - Operações entre arrays
2. Funções unárias universais
3. Funções binárias universais
4. Broadcasting
5. Funções NumPy comuns

#### Dia 71 - [Aplicações de NumPy - 4](./Day66-80/71.numpy-applications-4.md)

1. Vetores
2. Determinantes
3. Matrizes
4. Polinômios

#### Dia 72 - [pandas explicados de maneira simples - 1](./Day66-80/72.pandas-in-depth-1.md)

1. Criando objetos `Series`
2. Operações em objetos `Series`
3. Propriedades e métodos de objetos `Series`

#### Dia 73 - [pandas explicados de maneira simples - 2](./Day66-80/73.pandas-in-depth-2.md)

1. Criando objetos `DataFrame`
2. Propriedades e métodos de objetos `DataFrame`
3. Lendo e gravando dados em `DataFrame`

#### Dia 74 - [pandas explicados de maneira simples - 3](./Day66-80/74.pandas-in-depth-3.md)

1. Remodelação de dados
   - Concatenação de dados
   - Mesclagem de dados
2. Limpeza de dados
   - Valores ausentes
   - Valores duplicados
   - Valores discrepantes
   - Pré-processamento

#### Dia 75 - [pandas explicados de maneira simples - 4](./Day66-80/75.pandas-in-depth-4.md)

1. Dinamização de dados
   - Obtenção de estatísticas descritivas
   - Classificação e valores principais
   - Agrupamento e agregação
   - Tabelas dinâmicas e tabelas cruzadas
2. Apresentação de dados

#### Dia 76 - [pandas explicados de maneira simples - 5](./Day66-80/76.pandas-in-depth-5.md)

1. Cálculo de alterações ano a ano e período a período
2. Cálculos de janela
3. Determinando correlações

#### Dia 77 - [pandas explicados de maneira simples - 6](./Day66-80/77.pandas-in-depth-6.md)

1. Usando índices
   - Índices de intervalo
   - Índices categóricos
   - Índices multinível
   - Índices de intervalo
   - Índices de data e hora

#### Dia 78 - [Visualização de dados - 1](./Day66-80/78.data-visualization-1.md)

1. Instalando e importando matplotlib
2. Criando a tela
3. Criando os eixos
4. Desenhar gráficos
   - Gráficos de linhas
   - Gráficos de dispersão
   - Gráficos de barras
   - Gráficos de pizza
   - Histogramas
   - Gráficos de caixa
5. Exibindo e salvando gráficos

#### Dia 79 - [Visualização de dados - 2](./Day66-80/79.data-visualization-2.md)

1. Gráficos avançados
   - Gráficos de bolhas
   - Gráficos de área
   - Gráficos de radar
   - Gráficos de rosas
   - Gráficos 3D

#### Dia 80 - [Visualização de dados - 3](./Day66-80/80.data-visualization-3.md)

1. Seaborn
2. Gráficos

### Dia 81~90 - Aprendizado de Máquina

#### Dia 81 - [Uma breve discussão sobre aprendizado de máquina](./Day81-90/81.machine-learning-overview.md)

1. História da inteligência artificial
2. O que é aprendizado de máquina
3. Áreas de aplicação de aprendizado de máquina
4. Classificações de aprendizado de máquina
5. As etapas do aprendizado de máquina
6. Um primeiro exercício de aprendizado de máquina

#### Dia 82 - [Algoritmo k-vizinhos mais próximos](./Day81-90/82.k-nearest-neighbors.md)

1. Medição de distância
2. Introdução ao conjunto de dados
3. Implementando classificação kNN
4. Avaliação do modelo
5. Ajuste de parâmetros
6. Implementando regressão kNN

#### Dia 83 - [Árvores de Decisão e Florestas Aleatórias](./Day81-90/83.decision-trees-and-random-forest.md)

1. Construindo árvores de decisão
   - Seleção de recursos
   - Divisão de dados
   - Poda de árvores
2. Implementando um modelo de árvore de decisão
3. Visão geral de florestas aleatórias

#### Dia 84 - [Algoritmo Ingênuo de Bayes](./Day81-90/84.naive-bayes.md)

1. Teorema de Bayes
2. Ingênuo Bayes
3. Princípios do algoritmo
   - Estágio de treinamento
   - Estágio de previsão
   - Implementação de código
4. Vantagens e desvantagens do algoritmo

#### Dia 85 - [Modelos de regressão](./Day81-90/85.regression-models.md)

1. Categorias de modelos de regressão
2. Calculando coeficientes de regressão
3. Introdução a um novo conjunto de dados
4. Implementação de código de regressão linear
5. Avaliação de modelos de regressão
6. Apresentando termos de regularização
7. Outra implementação de regressão linear
8. Regressão polinomial
9. Regressão logística

#### Dia 86 - [Algoritmo de agrupamento K-Means](./Day81-90/86.k-means-clustering.md)

1. Princípios do algoritmo
2. Descrição matemática
3. Implementação de código

#### Dia 87 - [Algoritmos de aprendizagem em conjunto](./Day81-90/87.ensemble-learning.md)

1. Categorias de algoritmos
2. AdaBoost
3. GBDT
4. XGBoost
5. LightGBM

#### Dia 88 - [Modelos de redes neurais](./Day81-90/88.neural-network-models.md)

1. Composição básica
2. Princípios de funcionamento
3. Implementação de código
4. Vantagens e desvantagens do modelo

#### Dia 89 - [Introdução ao processamento de linguagem natural](./Day81-90/89.natural-language-processing-intro.md)

1. Modelo de saco de palavras
2. Vetores de palavras
3. NPLM e RNN
4. Seq2Seq
5. Transformador

#### Dia 90 - [Aprendizado de máquina na prática](./Day81-90/90.machine-learning-in-practice.md)

1. Exploração de dados
2. Engenharia de recursos
3. Treinamento de modelo
4. Avaliação do modelo
5. Implantação de modelo

### Dia 91~99 - [Desenvolvimento de projetos em equipe](./Day91-100)

#### Dia 91: [Problemas e soluções no desenvolvimento de projetos em equipe](./Day91-100/91.team-project-problems-and-solutions.md)

1. Modelos de processos de software
   - Modelo de processo clássico (modelo em cascata)
     - Análise de viabilidade (estudar se o projeto deve ou não ser feito), saída: "Relatório de Análise de Viabilidade"
     - Análise de requisitos (estudar o que deve ser construído), saída: "Especificação de Requisitos" e protótipos de interface do produto
     - Design de alto nível e design detalhado, saída: diagramas de modelo conceitual (diagramas ER), diagramas de modelo físico, diagramas de classes, diagramas de sequência e assim por diante
     - Codificação / testes
     - Lançamento / manutenção

     A maior desvantagem do modelo em cascata é que ele não lida bem com mudanças nos requisitos. O produto só aparece depois que todo o processo termina, o que reduz a motivação da equipe.
   - Desenvolvimento ágil (Scrum) – Product Owner, Scrum Master, desenvolvedores – Sprint
     - Backlog do produto (histórias de usuário, protótipos do produto)
     - Reuniões de planejamento (estimativa e orçamento)
     - Desenvolvimento diário (reuniões rápidas, técnica Pomodoro, programação em par, desenvolvimento orientado a testes, refatoração de código e assim por diante)
     - Correção de bugs (descrição do problema, passos de reprodução, testador, responsável)
     - Lançamentos de versão
     - Reuniões de revisão (demonstração, com participação dos usuários)
     - Reuniões de retrospectiva (resumo do ciclo de iteração atual)

     > Complemento: Manifesto para o Desenvolvimento Ágil de Software
     >
     > - **Indivíduos e interações** mais que processos e ferramentas
     > - **Software em funcionamento** mais que documentação abrangente
     > - **Colaboração com o cliente** mais que negociação de contratos
     > - **Responder a mudanças** mais que seguir um plano
     >
     ![](./res/agile-scrum-sprint-cycle.png)
     >
     > Papéis: product owner (decide o que será construído e tem autoridade para fechar requisitos), líder da equipe (resolve problemas diversos, melhora a forma de trabalho da equipe e protege o time de desenvolvimento de interferências externas) e equipe de desenvolvimento (executores do projeto, especialmente desenvolvedores e testadores).
     >
     > Trabalho preparatório: caso de negócio e financiamento, contratos, visão, requisitos iniciais do produto, plano inicial de lançamento, divisão societária e formação da equipe.
     >
     > Equipes ágeis geralmente têm de 8 a 10 pessoas.
     >
     > Estimativa de esforço: quantifique as tarefas de desenvolvimento, incluindo protótipos, design de logotipo, design de UI, desenvolvimento frontend e assim por diante. Divida cada item na menor unidade de tarefa possível; a referência é que a menor tarefa não deve levar mais de dois dias. Em seguida, estime a duração total do projeto. Coloque cada tarefa no quadro de tarefas, dividido em três partes: `a fazer`, `em andamento` e `concluído`.

2. Construindo a equipe do projeto
   - Composição e funções da equipe

     ![company_architecture](./res/company_architecture.png)

   - Padrões de programação e revisão de código (`flake8`, `pylint`)

     ![](./res/pylint.png)

    - Algumas "convenções" em Python (consulte [Convenções de programação Python – Como escrever código Python](./extras/python-programming-conventions.md))

   - Fatores que afetam a legibilidade do código:
     - Comentários insuficientes ou inexistentes
     - Código que viola as boas práticas da linguagem
     - Programação com antipadrões (código espaguete, programação por copiar e colar, programação arrogante, ...)

3. Introdução às ferramentas de desenvolvimento de equipe
   - Controle de versão: Git, Mercurial
   - Gerenciamento de defeitos: [Gitlab](https://about.gitlab.com/), [Redmine](http://www.redmine.org.cn/)
   - Ferramentas ágeis de circuito fechado: [ZenTao](https://www.zentao.net/), [JIRA](https://www.atlassian.com/software/jira/features)
   - Integração contínua: [Jenkins](https://jenkins.io/), [Travis-CI](https://travis-ci.org/)

Consulte [Problemas e soluções no desenvolvimento de projetos em equipe](./Day91-100/91.team-project-problems-and-solutions.md).

##### Seleção do tema do projeto e compreensão do negócio

1. Definindo o escopo do tópico
   - CMS (lado do cliente): sites de agregação de notícias, comunidades de perguntas e respostas/compartilhamento, sites de resenhas de filmes/resenhas de livros e assim por diante
   - MIS (lado do cliente + lado administrativo): KMS, sistemas de avaliação de KPI, HRS, sistemas de CRM, sistemas de cadeia de suprimentos, sistemas de gerenciamento de armazém e assim por diante
   - Back-ends de aplicativos (lado administrativo + APIs de dados): comércio de segunda mão, jornais e revistas, comércio eletrônico de nicho, notícias e informações, viagens, aplicativos sociais, aplicativos de leitura e assim por diante
   - Outros tipos: seu próprio histórico no setor e experiência de trabalho e domínios de negócios que são mais fáceis de entender e controlar

2. Compreender requisitos, dividir módulos e atribuir tarefas
   - Compreensão dos requisitos: brainstorming e análise da concorrência
   - Divisão de módulos: desenhar mapas mentais (XMind). Cada módulo é um nó de ramificação e cada função concreta é um nó folha (expresso com verbos). Certifique-se de que cada nó folha não possa ser dividido em novos nós. Determine a importância, prioridade e carga de trabalho de cada nó folha.
   - Atribuição de tarefas: o líder do projeto atribui tarefas a cada membro da equipe com base nos indicadores acima.

![](./res/requirements_by_xmind.png)

3. Criação do cronograma do projeto (atualizado diariamente)

    | Módulo | Função | Membro | Status | Feito | Horas | Início planejado | Início real | Fim planejado | Fim real | Notas |
   | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
    | Comentários | Adicionar comentário | Wang Dachui | Em andamento | 50% | 4 | 2018/8/7 |    | 2018/8/7 |    |    |
    |    | Excluir comentário | Wang Dachui | Esperando | 0% | 2 | 2018/8/7 |    | 2018/8/7 |    |    |
    |    | Ver comentário | Bai Yuanfang | Em andamento | 20% | 4 | 2018/8/7 |    | 2018/8/7 |    | Revisão de código necessária |
    |    | Votação de comentários | Bai Yuanfang | Esperando | 0% | 4 | 2018/8/8 |    | 2018/8/8 |    |    |

4. OOAD e design de banco de dados
   - Diagramas de classes UML

     ![uml](./res/uml-class-diagram.png)

   - Criando tabelas a partir de modelos (engenharia avançada)

     Por exemplo, em um projeto Django, você pode criar tabelas no banco de dados com os comandos abaixo.

     ```Shell
     python manage.py makemigrations app
     python manage.py migrate
     ```

   - Usando o PowerDesigner para desenhar diagramas de modelos físicos

     ![](./res/power-designer-pdm.png)

   - Criação de modelos a partir de tabelas de banco de dados (engenharia reversa)

     Por exemplo, em um projeto Django, você pode gerar modelos com o comando abaixo.

     ```Shell
     python manage.py inspectdb > app/models.py
     ```

#### Dia 92: [Explicação detalhada da tecnologia Docker Container](./Day91-100/92.docker-in-depth.md)

1. Introdução ao Docker
2. Instalando o Docker
3. Criação de containers com Docker (Nginx, MySQL, Redis, Gitlab, Jenkins)
4. Construindo imagens Docker (escrevendo Dockerfiles e diretivas relacionadas)
5. Orquestração de contêineres (Docker Compose)
6. Gerenciamento de cluster (Kubernetes)

#### Dia 93: [Otimização de desempenho MySQL](./Day91-100/93.mysql-performance-optimization.md)

1. Princípios básicos
2. O mecanismo InnoDB
3. Usando índices e os pontos a serem observados
4. Particionamento de dados
5. Otimização de SQL
6. Otimização de configuração
7. Otimização de arquitetura

#### Dia 94: [Design de interface de API de rede](./Day91-100/94.network-api-design.md)

1. Princípios de design
   - Principais questões
   - Outros problemas
2. Escrevendo documentação

#### Dia 95: [Desenvolvendo Projetos Comerciais com Django](./Day91-100/95.django-for-commercial-projects.md)

##### Problemas comuns no desenvolvimento de projetos

1. Configuração de banco de dados (vários bancos de dados, replicação mestre-escravo, roteamento de banco de dados)
2. Configuração de cache (cache particionado, configurações de chave, configurações de tempo limite, replicação mestre-escravo, failover com Sentinel)
3. Configuração de registro em log
4. Análise e depuração (barra de ferramentas Django Debug)
5. Módulos Python úteis (cálculo de data, processamento de imagem, criptografia de dados, APIs de terceiros)

##### Projeto de API REST

1. Arquitetura RESTful
   - [Compreendendo a arquitetura RESTful](http://www.ruanyifeng.com/blog/2011/09/restful.html)
   - [Guia de design de API RESTful](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
   - [Práticas recomendadas de API RESTful](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)
2. Escrevendo documentação da interface API
   - [RAP2](http://rap2.taobao.org/)
   - [YApi](http://yapi.demo.qunar.com/)
3. Aplicando [Django REST framework](https://www.django-rest-framework.org/)

##### Análise dos pontos-chave e difíceis do projeto

1. Usando cache para reduzir a pressão do banco de dados - Redis
2. Usando filas de mensagens para dissociar serviços e suavizar picos de tráfego - Celery + RabbitMQ

#### Dia 96: [Teste de software e testes automatizados](./Day91-100/96.software-testing-and-automation.md)

##### Teste de unidade

1. Tipos de testes
2. Gravação de testes unitários (`unittest`, `pytest`, `nose2`, `tox`, `ddt` e assim por diante)
3. Cobertura de teste (`coverage`)

##### Implantando Projetos Django

1. Preparativos antes da implantação
   - Configurações de chave (`SECRET_KEY` / `DEBUG` / `ALLOWED_HOSTS` / cache / banco de dados)
   - `HTTPS` / `CSRF_COOKIE_SECURE` / `SESSION_COOKIE_SECURE`
   - Configuração relacionada ao log
2. Revisão de comandos comuns do Linux
3. Instalação e configuração de serviços Linux comuns
4. Usando uWSGI/Gunicorn e Nginx
   - Comparação entre Gunicorn e uWSGI
     - Para aplicações simples que não precisam de muita personalização, Gunicorn é uma boa escolha. A curva de aprendizado do uWSGI é muito mais íngreme que a do Gunicorn, e os parâmetros padrão do Gunicorn já atendem à maioria das aplicações.
     - uWSGI oferece suporte a implantação heterogênea.
     - Como o próprio Nginx oferece suporte a uWSGI, em produção Nginx e uWSGI geralmente são implantados juntos; o uWSGI é um middleware WSGI completo e altamente personalizável.
     - Em desempenho, Gunicorn e uWSGI são bastante próximos.
5. Implantando ambientes de teste e produção com tecnologia de virtualização (Docker)

##### Teste de desempenho

1. Usando AB
2. Usando SQLslap
3. Usando Sysbench

##### Teste Automatizado

1. Usando Shell e Python para testes automatizados
2. Usando Selenium para testes automatizados
   - Selenium IDE
   - Selenium WebDriver
   - Selenium RC
3. Introdução ao Robot Framework

#### Dia 97: [Análise dos principais pontos técnicos para sites de comércio eletrônico](./Day91-100/97.ecommerce-site-architecture.md)

1. Modelos de negócios e requisitos principais
2. Design de modelo físico
3. Login de terceiros
4. Pré-aquecimento de cache e cache de consulta
5. Implementação de carrinho de compras
6. Integração de pagamento
7. Problemas de venda relâmpago e vendas excessivas
8. Gerenciamento de recursos estáticos
9. Soluções de pesquisa de texto completo

#### Dia 98: [Implantação de projetos e ajuste de desempenho](./Day91-100/98.deployment-and-performance-tuning.md)

1. Ajuste de banco de dados MySQL
2. Otimização de desempenho do servidor web
   - Configuração de balanceamento de carga Nginx
   - Usando Keepalived para obter alta disponibilidade
3. Ajuste de desempenho de código
   - Multithreading
   - Assincronização
4. Otimização de acesso a recursos estáticos
   - Armazenamento em nuvem
   - CDN

#### Dia 99: [Perguntas comuns da entrevista](./Day91-100/99.common-interview-questions.md)

1. Fundamentos da ciência da computação
2. Fundamentos do Python
3. Perguntas relacionadas a frameworks web
4. Perguntas relacionadas a rastreadores
5. Análise de dados
6. Perguntas relacionadas ao projeto

### Dia 100 - [Conteúdo Suplementar](./Day91-100/100.supplementary-content.md)

- Manuais de entrevistas
  - Manual de entrevistas em Python
  - Manual de entrevista SQL (para analistas de dados)
  - Manual de entrevista de análise de negócios
  - Manual de entrevista de aprendizado de máquina
- Fundamentos matemáticos do aprendizado de máquina
- Aprendizado profundo
  - Visão computacional
  - Grandes modelos de linguagem
