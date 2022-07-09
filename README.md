# lista-4-ces22 Sistema da Livraria

Vamos desenvolver um sistema de livraria que retornará no terminal as operações realizadas

## Diagrama de classes:
 - A classe Author e Client tem uma base comum de nome, email, por isso vão herdar de uma mesma classe, que poderia ser utilizado até para a adição de novos agentes seguindo o Principio de Liskov.
 - A classe TaxCalculator têm a função de calculateTax, que segue o principio do Open Closed, onde a função chamada em Livros não precisa ser modificada, enquanto isso poderiamos criar novas funções de taxa ou até mesmo uma interface para uma calculadora de impostos. No problema decidi somente pela Classe para simplificar o projeto e com um método mais genérico que chama dois métodos particulares.

<img src="./livraria-Page-2.drawio.svg">

## Classes e testes

### Classe Person e derivados
Para a entrada:

```
if __name__ == '__main__':
    p1 = Person('Wagner', 'wagner@gmail.com')
    print(p1)
    # change attributes
    p1.update(nome='Moura')
    print(p1)
    p1.update(email='moura@gmail.com')
    print(p1)
    print('')

    c1 = Client('jonas','jonas@gmail.com')
    c1.addCompra('O principe R$ 30,00')
    print(c1)
    print('')

    a1 = Author('maquiavel', 'maquiavel@gmail.com')
    a1.addTitulo('O principe')
    print(a1)
    print('')
```

Temos a seguinte saída observando que as entradas dadas foram strings pela flexibilidade do Python, porém na implementação mais completa serão realmente objetos do tipo Compra e Titulos.

```
Pessoa: Wagner Email: wagner@gmail.com
Pessoa: Moura Email: wagner@gmail.com
Pessoa: Moura Email: moura@gmail.com

Pessoa: jonas Email: jonas@gmail.com comprou:
 - O principe R$ 30,00

Pessoa: maquiavel Email: maquiavel@gmail.com escreveu:
 - O principe

```

## Classe TaxCalculator

A classe faz a implementação dos calculos das taxas e para entrada:

```
if __name__ == '__main__':
    
    tax = TaxCalculator()
    print('Imposto para compra a R$ 20,00 e venda a R$ 30,00 do genêro Fantasia:')
    print('R$ {:.2f}'.format(tax.calculateTax(20.0, 30.0, 'Fantasia')))
    print('')

    print('Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Fantasia')
    print('R$ {:.2f}'.format(tax.calculateTax(20, 40, 'Fantasia')))
    print('')

    print('Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Clássicos Brasileiros')
    print('R$ {:.2f}'.format(tax.calculateTax(20, 40, 'Clássicos Brasileiros')))
    print('')
```

Tem o seguinte Output:

```
Imposto para compra a R$ 20,00 e venda a R$ 30,00 do genêro Fantasia:
R$ 3.00

Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Fantasia
R$ 6.00

Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Clássicos Brasileiros
R$ 4.00

```


### Interface Produtos e Livros