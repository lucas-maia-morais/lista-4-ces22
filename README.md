# lista-4-ces22 Sistema da Livraria

Vamos desenvolver um sistema de livraria que retornará no terminal as operações realizadas

## Diagrama de classes:
 - A classe Author e Client tem uma base comum de nome, email, por isso vão herdar de uma mesma classe, que poderia ser utilizado até para a adição de novos agentes seguindo o Principio de Liskov.
 -

<img src="./livraria-Page-2.drawio.svg">

## Classes e testes

### Classe Person e derivados
Para a entrada:

```
if __name__ == '__main__':
    p1 = Person('Wagner', 'wagner@gmail.com')
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

Pessoa: jonas Email: jonas@gmail.com comprou:
 - O principe R$ 30,00

Pessoa: maquiavel Email: maquiavel@gmail.com escreveu:
 - O principe

```