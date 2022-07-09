from __future__ import annotations
from abc import ABC, abstractmethod

class Person(ABC):

    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    
    def update(self, nome, email):
        self.nome = nome
        self.email

    def __str__(self) -> str:
        return 'Pessoa: ' + self.nome + ' Email: ' + self.email

class Client(Person):

    def __init__(self, nome, email):
        self.compras = []
        super().__init__(nome, email)

    def update(self, nome, email):
        return super().update(nome, email)

    def addCompra(self,compra):
        self.compras.append(compra)

    def __str__(self) -> str:
        return super().__str__() + ' comprou:\n' + f'\n'.join([' - '+str(c) for c in self.compras])


class Author(Person):

    def __init__(self, nome, email):
        self.titulos = []
        super().__init__(nome, email)

    def update(self, nome, email):
        return super().update(nome, email)
    
    def addTitulo(self, livro):
        self.titulos.append(livro)

    def __str__(self) -> str:
        return super().__str__() + ' escreveu:\n' + f'\n'.join([' - '+str(t) for t in self.titulos])

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