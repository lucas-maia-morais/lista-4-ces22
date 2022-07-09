from __future__ import annotations
from abc import ABC, abstractmethod
from http.client import PRECONDITION_FAILED

from TaxCalculator import TaxCalculator
from Person import Author

class Product(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self, **attributes) -> None:
        pass

    @abstractmethod
    def preco(self) -> float:
        pass

    # Funciona como identificado também
    @abstractmethod
    def __str__(self) -> str:
        pass
    
    @abstractmethod
    def getDescription(self) -> str:
        pass


class Livro(Product):

    def __init__(self, titulo, autor, genero, edicao, preco_venda, preco_compra, impostos):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.edicao = edicao
        self.preco_venda = preco_venda
        self.preco_compra = preco_compra
        self.impostos = impostos
    
    def update(self, **attributes) -> None:
        for attribute, value in attributes.items():
            if hasattr(self, attribute):
                setattr(self, attribute, value)
            else:
                raise AttributeError(f'{self.__name__} has no attribute: {attribute}')

    def preco(self) -> float:
        return self.preco_venda + self.impostos.calculateTax(self.preco_compra, self.preco_venda, self.genero)

    def __str__(self) -> str:
        return self.titulo

    def getDescription(self) -> str:
        description = 'Titulo: ' + self.titulo     + '\n' + \
                      'Autor:  ' + str(self.autor) + '\n' + \
                      'Genero: ' + self.genero     + '\n' + \
                      'Edicao: ' + self.edicao     + '\n' + \
                      'Preço de Venda     :' + 'R$ {:.2f}'.format(self.preco_venda) + '\n' \
                      'Preço de Compra    :' + 'R$ {:.2f}'.format(self.preco_compra) + '\n' \
                      'Impostos           :' + 'R$ {:.2f}'.format(self.impostos.calculateTax(self.preco_compra, self.preco_venda, self.genero)) + '\n' + \
                      'Preço final Cliente: ' + 'R$ {:.2f}'.format(self.preco()) + '\n'

        return description

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

    print('\n=====================Livro 2 Final ======================')
    print(l2.getDescription())
