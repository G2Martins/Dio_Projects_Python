# Desafio de Código: Sistema de Gerenciamento de Vendas (POO)

## Descrição
Você está desenvolvendo um sistema para gerenciar dados de vendas que serão posteriormente importados para o Power BI. Você tem a estrutura de duas classes, `Venda` e `Relatorio`, já definidas. Sua tarefa é implementar partes específicas do código dentro dessas classes para garantir a integridade dos dados e realizar cálculos financeiros básicos.

### Detalhamento:

**1. Classe Relatorio - Método `adicionar_venda`:**
* Implemente uma verificação de segurança. O método deve verificar se o objeto passado como argumento é realmente uma instância da classe `Venda`.
* Apenas se essa verificação for verdadeira, o objeto deve ser adicionado à lista interna `self.vendas`.

**2. Classe Relatorio - Método `calcular_total_vendas`:**
* Itere sobre a lista de vendas armazenadas.
* Para cada item, calcule o subtotal multiplicando a `quantidade` pelo `valor`.
* Acumule esse resultado em uma variável `total` e retorne o valor final.

**3. Função `main`:**
* Após a coleta dos dados e criação dos objetos, chame o método de cálculo e exiba o resultado no formato padrão exigido.

### Entrada
A entrada consiste em dados de vendas (repetidos 3 vezes) com:
* Produto (string)
* Quantidade (inteiro)
* Valor (decimal)

### Saída
A saída é uma string contendo o texto "Total de Vendas:" seguido do valor numérico calculado.

### Exemplos
| Entrada | Saída |
| --- | --- |
| Notebook<br>3<br>1500.00<br>Mouse<br>10<br>50.00<br>Teclado<br>5<br>100.00 | Total de Vendas: 5500.0 |
| Monitor<br>2<br>800.00<br>Webcam<br>1<br>120.00<br>Fone de Ouvido<br>4<br>75.00 | Total de Vendas: 2020.0 |

---

## Explicação do Código

Este desafio foca em **Programação Orientada a Objetos (POO)** e encapsulamento de lógica.

### 1. Verificação de Tipo (`isinstance`)
No método `adicionar_venda`, utilizamos a função nativa `isinstance(objeto, Classe)`.
```python
if isinstance(venda, Venda):
    self.vendas.append(venda)