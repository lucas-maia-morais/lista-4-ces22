from __future__ import annotations
from http.client import PRECONDITION_FAILED
from Product import Livro
from Person import Author
from TaxCalculator import TaxCalculator

class Compra:

    def __init__(self):
        self.items = {}
    
    def add(self, produto, qtd):
        self.items[produto] = {'qtd': qtd, 'preco': produto.preco()}
    
    def remove(self, produto):
        self.items.pop(produto)

    def __str__(self) -> str:
        ''.join(['\nLivro: {} \n\t Estoque:     {} \nt preço     {}\n\t preço total    {}\n'\
            .format(key, self.items[key]['qtd'],\
            self.items[key]['preco'],\
            self.items[key]['qtd']*self.items[key]['preco'])  for key in self.items.keys()])
        nota_fiscal = '================= NOTA FISCAL ================='
        preco_total = 0
        for key in self.items.keys():
            p = self.items[key]['preco']
            q = self.items[key]['qtd']
            preco_total += p*q
            nota_fiscal = nota_fiscal + '\nProduto     :    {} \n  Estoque   :    {} \n  Preço Uni.: R$ {:.2f}\nPreço         R$ {}\n'\
            .format(key, q, p,p*q)
        nota_fiscal = nota_fiscal + '\nPREÇO FINAL : R$ {:.2f}\n'.format(preco_total)
        nota_fiscal += '==============================================='
        return nota_fiscal

if __name__ == '__main__':
    a1 = Author('Maquiavel', 'maquiavel@gmail.com')
    i1 = TaxCalculator()
    l1 = Livro('O Principe', a1, 'Estrátegia', '45ª', 40, 20, i1)
    a2 = Author('Rick Riordan', 'rickriordan@gmail.com')
    i2 = TaxCalculator()
    l2 = Livro('Percy Jackson e o Ladrão de raios', a2, 'Fantasia', '45ª', 50, 20, i1)

    e = Compra()
    e.add(l1, 5)
    e.add(l2, 1)
    print(e)

    e.remove(l2)
    print(e)

    l2.update(preco_venda = 100)
    print(e)