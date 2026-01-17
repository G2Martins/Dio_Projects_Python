# Desafio de Código: Identificando o Produto Mais Vendido

## Descrição
Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido, que será usado para destacar produtos populares no relatório do Power BI.

### Detalhamento:
**1. Encontre o produto com a maior contagem:**
* Itere sobre o dicionário `contagem`, que contém a contagem de cada produto.
* Compare a contagem atual com a contagem máxima armazenada em `max_count`.
* Se a contagem atual for maior que `max_count`, atualize `max_count` e defina `max_produto` como o produto atual.

**2. Converter a entrada em uma lista de strings, removendo espaços extras:**
* Use o método `split(',')` para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.
* Utilize uma **list comprehension** para remover espaços em branco extras ao redor de cada string, usando o método `strip()`.

### Entrada
Uma lista de strings onde cada string representa o nome de um produto vendido.

### Saída
A string com o nome do produto mais vendido. Se houver empate, retorne qualquer um dos produtos mais vendidos.

### Exemplos
| Entrada | Saída |
| --- | --- |
| Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado | Mouse |
| Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora | Impressora |
| Webcam, Webcam, Headset, Monitor, Headset, Headset | Headset |

---

## Explicação do Código

A solução aborda o problema de frequência (contagem de ocorrências) muito comum em análise de dados.

### 1. Tratamento de Dados (`obter_entrada_produtos`)
O desafio exige uma limpeza dos dados (Data Cleaning) logo na entrada. Como o usuário digita os produtos separados por vírgula, é comum haver espaços indesejados (ex: `"Mouse, Teclado"` vira `["Mouse", " Teclado"]`).
* **List Comprehension**: A estrutura `[item.strip() for item in entrada.split(',')]` resolve isso em uma linha.
    * `split(',')`: Separa a string original.
    * `strip()`: Remove os espaços em branco do início e do fim de cada palavra individualmente, garantindo que `" Teclado"` se torne `"Teclado"`.

### 2. Lógica de Máximo (`produto_mais_vendido`)
Após contar as ocorrências e armazená-las em um dicionário (onde a chave é o nome do produto e o valor é a quantidade), precisamos descobrir qual chave tem o maior valor.
* **Iteração**: O código percorre cada par `chave, valor` do dicionário usando `.items()`.
* **Comparação**: A variável `max_count` guarda o maior número visto até agora. Se o produto atual tiver uma contagem superior a `max_count`, ele assume o posto de "líder" (`max_produto`).