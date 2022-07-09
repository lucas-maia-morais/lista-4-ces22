from __future__ import annotations
from ast import Str
from http.client import PRECONDITION_FAILED

from Product import Livro
from Person import Author, Client
from TaxCalculator import TaxCalculator
from Estoque import Estoque
from Compra import Compra

class Padaria():
    
    def __init__(self):
        self.estoque = Estoque()
        self.compras = []
        self.clientes = []
    
    def addClient(self, client: Client)-> bool:
        if not (client in self.clientes):
            self.clientes.append(client)
            return True
        return False

    def updateClient(self, client: Client, **atributes):
        if client in self.clientes:
            client.update(**atributes)
            return True
        return False
    
    def removeClient(self, client: Client, **atributes):
        if client in self.clientes:
            for idx in range(len(self.clientes)):
                if client == self.clientes[idx]:
                    self.clientes.pop(idx)
                    break
            return True
        return False

    def searchClient(self, name: Str) -> Client:
        for client in self.clientes:
            if(name == client.nome):
                return client
        return None


    def addBook(self, book: Livro, qtd)-> bool:
        if self.estoque.search(book) < 0:
            self.estoque.add(book)
            self.estoque.atualizar(book, qtd)
            return True
        return False

    def updateBook(self, book: Livro,  **atributes)-> bool:
        if self.estoque.search(book) < 0:
            return False
        book.update()
        return True

    def deleteBook(self, book: Livro)-> bool:
        if self.estoque.search(book) < 0:
            return False
        self.estoque.remove(book)
        return True

    def searchByAuthor(self, author: Author)-> Livro:
        titulos = []
        titulosAutor = author.getTitulos()
        for titulo in titulosAutor:
            qtd = self.estoque.search(titulo)
            if qtd > 0:
                titulos.append(titulo)

        return titulos

    def searchBook(self, titulo: str) -> Livro:
        for titulo_estoque in self.estoque.estoque.keys():
            if (titulo == titulo_estoque):
                return titulo_estoque
        return None

    def addCompra(self, client: Client, compra: Compra) -> bool:
        for titulo in compra.items.keys():
            if compra.items[titulo]['qtd'] > self.estoque.estoque[titulo]:
                return False
        for titulo in compra.items.keys():
            self.estoque.atualizar(titulo, -compra.items[titulo]['qtd'])
        client.addCompra(compra)
        self.compras.append(compra)
        return True

    def removeCompra(self, client: Client, compra: Compra) -> bool:
        if compra in self.compras:
            for titulo in compra.items.keys():
                self.estoque.atualizar(titulo, compra.items[titulo]['qtd'])

            for idx in range(len(self.compras)):
                if compra == self.compras[idx]:
                    self.compras.pop(idx)
                    break

            for idx in range(len(client.compras)):
                if compra == client.compras[idx]:
                    client.compras.pop(idx)
                    break
            
            return True
        else:
            return False

    def __str__(self):
        s = "============================= Situação da Padaria ==========================\n"
        s += "------------------------------- Estoque --------------------------------------\n"
        s += str(self.estoque)
        s += "------------------------------- Clientes --------------------------------------\n"
        for c in self.clientes:
            s += '\n +' + str(c)
        s += "-------------------------------  Compras  -------------------------------------\n"
        for co in self.compras:
            s += str(co)
        return s

if __name__ == '__main__':

    p = Padaria()
    
    a1 = Author('Maquiavel', 'maquiavel@gmail.com')
    i1 = TaxCalculator()
    l1 = Livro('O Principe', a1, 'Estrátegia', '45ª', 40, 20, i1)
    a1.addTitulo(l1)
    p.addBook(l1, 20)

    a2 = Author('Rick Riordan', 'rickriordan@gmail.com')
    i2 = TaxCalculator()
    l2 = Livro('Percy Jackson e o Ladrão de raios', a2, 'Fantasia', '45ª', 50, 20, i1)
    l3 = Livro('Percy Jackson e o Mar de Monstros', a2, 'Fantasia', '45ª', 50, 20, i1)
    l4 = Livro('Percy Jackson e a Maldição do Titã', a2, 'Fantasia', '45ª', 50, 20, i1)
    a2.addTitulo(l2)
    p.addBook(l2, 15)
    a2.addTitulo(l3)
    p.addBook(l3, 25)
    a2.addTitulo(l4)
    p.addBook(l4, 30)

    print('\n------------------ Buscas -----------------------')
    booksa2 = p.searchByAuthor(a2)
    for b in booksa2:
        print(b)

    print(p)

    c1 = Client('Marcio', 'marcio@gmail.com')
    c2 = Client('José', 'jose@gmail.com')
    p.addClient(c1)
    p.addClient(c2)

    print(p)

    e1 = Compra()
    e1.add(l1, 5)
    e1.add(l2, 1)

    p.addCompra(c1, e1)

    print(p)


    p.removeCompra(c1, e1)

    print(p)

    p.deleteBook(l4)
    p.deleteBook(l3)
    p.removeClient(c2)

    print(p)

    # e.remove(l2)
    # print(e)

    # l2.update(preco_venda = 100)
    # print(e)