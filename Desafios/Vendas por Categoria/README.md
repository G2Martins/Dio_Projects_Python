# Desafio de Código: Agrupamento de Vendas por Categoria

## Descrição
Você está desenvolvendo um sistema para organizar vendas por categorias antes de gerar um relatório. O objetivo é criar uma classe `Categoria` que gerencie as vendas associadas a uma determinada categoria e calcule o total de vendas dessa categoria.

### Detalhamento:

**1. Classe Categoria - Método `adicionar_venda`:**
* Recebe um objeto `Venda`.
* Deve armazenar esse objeto em uma lista interna (`self.vendas`).

**2. Classe Categoria - Método `total_vendas`:**
* Percorre a lista de vendas da categoria.
* Soma o atributo `valor` de cada venda.
* **Atenção à Regra de Negócio:** Conforme o enunciado, o valor fornecido na entrada já representa o total daquele lote de produtos (ex: 5 Celulares custaram 1000 no total, e não 1000 cada). Portanto, **não** se deve multiplicar quantidade por valor neste cálculo.

**3. Função `main`:**
* Gerencia a entrada de dados (loops para categorias e vendas).
* Instancia os objetos `Venda` e `Categoria`.
* Exibe o resultado final formatado.

### Entrada
A entrada consiste em:
* Nome da Categoria (string)
* 2 linhas de vendas para aquela categoria, contendo: Produto, Quantidade, Valor Total.
*(O processo se repete para 2 categorias)*

### Saída
A saída deve exibir o total acumulado por categoria no formato: `Vendas em [Categoria]: [Valor]`

### Exemplos
| Entrada | Saída |
| --- | --- |
| Eletrônicos<br>Celular, 5, 1000<br>Fone de Ouvido, 10, 500<br>Móveis<br>Mesa, 2, 800<br>Cadeira, 4, 400 | Vendas em Eletrônicos: 1500.0<br>Vendas em Móveis: 1200.0 |
| Alimentos<br>Arroz, 10, 200<br>Feijão, 7, 140<br>Jardinagem<br>Planta, 2, 60<br>Ferramentas, 1, 100 | Vendas em Alimentos: 340.0<br>Vendas em Jardinagem: 160.0 |

---

## Explicação das Correções no Código

A principal alteração em relação à lógica comum foi no método `total_vendas`.

```python
def total_vendas(self):
    total = 0
    for venda in self.vendas:
        total += venda.valor # Correto segundo o enunciado
        # total += venda.quantidade * venda.valor -> INCORRETO para este desafio específico
    return total