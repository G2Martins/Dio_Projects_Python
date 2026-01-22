# Desafio de Código: Normalização de Tipos de Visuais no Power BI

## Descrição
Você tem uma lista de tipos de visuais e precisa processar essa lista para remover duplicatas e normalizar os nomes dos visuais. O objetivo é garantir que cada visual apareça apenas uma vez na lista e que todos os nomes estejam em um formato uniforme (Título Capitalizado).

### Detalhamento da Tarefa:

1.  **Normalizar Nomes**: Converter entradas como "gráfico de barras" ou "Gráfico de barras" para um padrão uniforme: "Gráfico De Barras" (todas as palavras iniciadas com maiúscula).
2.  **Remover Duplicatas**: Garantir que, após a normalização, cada tipo de visual apareça apenas uma vez.
3.  **Ordenação**: A lista final deve estar organizada alfabeticamente para consistência.

### Entrada
Uma string única contendo tipos de visuais separados por vírgula e espaço.
*Exemplo:* `Gráfico de Barras, gráfico de barras, Tabela`

### Saída
Uma string única com os visuais normalizados, únicos e separados por vírgula e espaço.
*Exemplo:* `Gráfico De Barras, Tabela`

### Exemplos de Teste
| Entrada | Saída |
| --- | --- |
| Gráfico de Barras, Gráfico de Barras, Tabela, Gráfico de Pizza, gráfico de barras | Gráfico De Barras, Gráfico De Pizza, Tabela |
| Gráfico de Linhas, gráfico de linhas, Tabela, tabela, gráfico de Linhas, Tabela Dinâmica | Gráfico De Linhas, Tabela, Tabela Dinâmica |
| gráfico de pizza, Gráfico de Pizza, gráfico de pizza, gráfico de colunas, Gráfico de Barras, gráfico de colunas | Gráfico De Barras, Gráfico De Colunas, Gráfico De Pizza |

---

## Explicação do Código

A solução utiliza conceitos fundamentais de manipulação de strings e coleções em Python para resolver o problema de ETL (Extração, Transformação e Carregamento) leve.

### 1. Set Comprehension (Conjuntos)
Para remover duplicatas e normalizar ao mesmo tempo, utilizamos um *Set Comprehension*:
```python
set_visuais = {visual.strip().title() for visual in visuais}