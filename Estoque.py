from __future__ import annotations
from Product import Livro
from Person import Author
from TaxCalculator import TaxCalculator

class Estoque():
    
    def __init__(self) -> None:
        self.estoque = {}

    def add(self, product) -> bool:
        self.estoque[product] = 0
        return True

    def atualizar(self, product, qtd) -> bool:
        if not product in self.estoque.keys():
            return False
        elif self.estoque[product]+qtd < 0:
            return False
        else:
            self.estoque[product] = self.estoque[product] + qtd
    
    def search(self, product) -> int:
        if not product in self.estoque.keys():
            return -1
        else:
            return self.estoque[product]

    def remove(self, product) -> bool:
        if not product in self.estoque.keys():
            return False
        else:
            self.estoque.pop(product)
            return True

    def __str__(self) -> str:
        return ''.join(['Livro: {} | Estoque: {}\n'.format(key, self.estoque[key]) for key in self.estoque.keys()])

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