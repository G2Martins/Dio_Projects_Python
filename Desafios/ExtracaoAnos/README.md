# Desafio de Código: Extração de Anos em Datas

## Descrição
Neste desafio, você precisa processar uma lista de datas fornecida pelo usuário para extrair o ano de cada uma delas. A extração de anos pode ser útil para diversas aplicações, como a realização de análises anuais em grandes volumes de dados temporais.

### Passo a Passo:
1. **Entrada de Dados:** O usuário fornecerá uma sequência de datas no formato "YYYY-MM-DD", onde "YYYY" representa o ano, "MM" o mês, e "DD" o dia. Todas as datas serão fornecidas em uma única linha, separadas por vírgula e espaço.
2. **Processamento dos Dados:** O objetivo é isolar a parte correspondente ao ano de cada data. Isso pode ser feito dividindo cada string de data pelo caractere `-` e selecionando a primeira parte.
3. **Formatação da Saída:** Após extrair os anos, você deve retorná-los como uma nova lista, onde os anos estão separados por vírgulas, mantendo a ordem original.

### Entrada
Uma lista de datas no formato "YYYY-MM-DD" separados por vírgula e espaço.

### Saída
Uma lista com os anos extraídos, separados por vírgula e espaço.

### Exemplos
| Entrada | Saída |
| --- | --- |
| 2024-01-01, 2023-07-19 | 2024, 2023 |
| 2022-12-31, 2021-01-01, 2020-05-25 | 2022, 2021, 2020 |
| 2025-09-09, 2025-10-10, 2026-03-03, 2027-07-07 | 2025, 2025, 2026, 2027 |

---

## Explicação do Código

Este desafio foca na manipulação de strings, uma habilidade essencial para limpeza de dados (Data Cleaning) antes de importá-los para ferramentas como Power BI ou bancos de dados.

### A Lógica de Extração (`split`)

A principal operação ocorre dentro da **list comprehension**:
```python
anos = [data.split("-")[0] for data in lista_datas]