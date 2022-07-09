# lista-4-ces22 Sistema da Livraria

Vamos desenvolver um sistema de livraria que retornará no terminal as operações realizadas

## Diagrama de classes:
 - A classe Author e Client tem uma base comum de nome, email, por isso vão herdar de uma mesma classe, que poderia ser utilizado até para a adição de novos agentes seguindo o Principio de Liskov.
 - A classe TaxCalculator têm a função de calculateTax, que segue o principio do Open Closed, onde a função chamada em Livros não precisa ser modificada, enquanto isso poderiamos criar novas funções de taxa ou até mesmo uma interface para uma calculadora de impostos. No problema decidi somente pela Classe para simplificar o projeto e com um método mais genérico que chama dois métodos particulares.
 - A classe Livro é implementada a partir da classe produto, pois como foi enunciado a livraria pode passar a vender novos produtos, então queremos basicamente nesse caso preco e identificacao do produto, e realizar operações básicas de criar e editar, o delete é basicamente retirar o elemento da lógica do programa. Coloquei uma função opcional getDescription para printar informações dos atributos da classe implementada usando a interface. Entende-se aqui que o valor final do produto para o cliente é o preco de venda do produto para livraria mais impostos.
 - A seguir vamos criar a classe estoque, ela poderia por exemplo ser conectada a um bando de dados para salvar os dados de interesse com relação ao estoque de produtos. Nela vamos implementar um simples dicionário com os produto e a quantidade de estoque presente. Teremos métodos de adicionar produtos ao estoque(add) e remover(remove) e atualizar estoque(atualizar) e busca(search), que retorna -1 caso não encontre e o estoque caso encontre. Em caso de falha para as operações de adição e atualização são retornados false e a operação não é feita.

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

### Classe TaxCalculator

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

Para a entrada a seguir:

```
if __name__ == '__main__':
    print('============== Livro 1 ====================')
    a1 = Author('Maquiavel', 'maquiavel@gmail.com')
    i1 = TaxCalculator()
    l1 = Livro('O Principe', a1, 'Estrátegia', '45ª', 40, 20, i1)
    print(l1.getDescription())

    print('\n============== Livro 2  adicionando livro ao Autor ====================')
    a2 = Author('Rick Riordan', 'rickriordan@gmail.com')
    i2 = TaxCalculator()
    l2 = Livro('Percy Jackson e o Ladrão de raioz', a2, 'Estrátegia', '45ª', 100, 20, i1)
    a2.addTitulo(l2)
    print(l2.getDescription())
    
    print('\n============== Correção (e.g. update do nome errdo) ====================')
    print(l2)
    l2.update(titulo='Percy Jackson e o Ladrão de raios')
    print(l2)

    print('\n============== Atualização do Preço ====================')
    print(l2)
    print('Preço final Cliente     : ' + 'R$ {:.2f}'.format(l2.preco()) + '')
    l2.update(preco_venda=50)
    print('Preço novo final Cliente: ' + 'R$ {:.2f}'.format(l2.preco()) + '')

    print('\n===================== Livro 2 Final ======================')
    print(l2.getDescription())
```


```
============== Livro 1 ====================
Titulo: O Principe
Autor:  Pessoa: Maquiavel Email: maquiavel@gmail.com escreveu:

Genero: Estrátegia
Edicao: 45ª
Preço de Venda     :R$ 40.00
Preço de Compra    :R$ 20.00
Impostos           :R$ 4.00
Preço final Cliente: R$ 44.00


============== Livro 2  adicionando livro ao Autor ====================
Titulo: Percy Jackson e o Ladrão de raioz
Autor:  Pessoa: Rick Riordan Email: rickriordan@gmail.com escreveu:
 - Percy Jackson e o Ladrão de raioz
Genero: Estrátegia
Edicao: 45ª
Preço de Venda     :R$ 100.00
Preço de Compra    :R$ 20.00
Impostos           :R$ 16.00
Preço final Cliente: R$ 116.00


============== Correção (e.g. update do nome errdo) ====================
Percy Jackson e o Ladrão de raioz
Percy Jackson e o Ladrão de raios

============== Atualização do Preço ====================
Percy Jackson e o Ladrão de raios
Preço final Cliente     : R$ 116.00
Preço novo final Cliente: R$ 56.00

===================== Livro 2 Final ======================
Titulo: Percy Jackson e o Ladrão de raios
Autor:  Pessoa: Rick Riordan Email: rickriordan@gmail.com escreveu:
 - Percy Jackson e o Ladrão de raios
Genero: Estrátegia
Edicao: 45ª
Preço de Venda     :R$ 50.00
Preço de Compra    :R$ 20.00
Impostos           :R$ 6.00
Preço final Cliente: R$ 56.00
```

### Classe Estoque

Para a seguinte entrada na qual testamos cada função implementada:

```
if __name__ == '__main__':
    a1 = Author('Maquiavel', 'maquiavel@gmail.com')
    i1 = TaxCalculator()
    l1 = Livro('O Principe', a1, 'Estrátegia', '45ª', 40, 20, i1)
    a2 = Author('Rick Riordan', 'rickriordan@gmail.com')
    i2 = TaxCalculator()
    l2 = Livro('Percy Jackson e o Ladrão de raios', a2, 'Estrátegia', '45ª', 50, 20, i1)

    e = Estoque()
    e.add(l1)
    e.add(l2)
    print(e)

    e.atualizar(l1, 10)
    print(e)

    e.atualizar(l2, -8)
    e.atualizar(l1, -8)
    print(e)

    e.remove(l2)
    print(e)

    print(e.search(l2))
    print(e.search(l1))
```

Temos a seguinte saída esperada:

```
Livro: O Principe | Estoque: 0
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

(base) lucas@Lucas:~/Documentos/1-ITA/2022.1/CES22/lista-4-ces22/lista-4-ces22$ python new_classes/Estoque.py 
Livro: O Principe | Estoque: 0
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: Teste | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

(base) lucas@Lucas:~/Documentos/1-ITA/2022.1/CES22/lista-4-ces22/lista-4-ces22$ python new_classes/Estoque.py 
Livro: O Principe | Estoque: 0
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

(base) lucas@Lucas:~/Documentos/1-ITA/2022.1/CES22/lista-4-ces22/lista-4-ces22$ python new_classes/Estoque.py 
Livro: O Principe | Estoque: 0
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 2
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 2

-1
(base) lucas@Lucas:~/Documentos/1-ITA/2022.1/CES22/lista-4-ces22/lista-4-ces22$ python new_classes/Estoque.py 
Livro: O Principe | Estoque: 0
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 10
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 2
Livro: Percy Jackson e o Ladrão de raios | Estoque: 0

Livro: O Principe | Estoque: 2

-1
2    
```