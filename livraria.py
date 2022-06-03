import Livro
import Autor
import Cliente
import Compra

class Livraria:
    def __init__(self):
        self.produtos = {}
        self.clientes = {}
        self.autores = {}
        self.compras = []
        self.pid = 0
        self.cid = 0
        self.aid = 0
        self.coid = 0

    def add_livro(self, info):
        info['id'] = self.pid
        livro = Livro(info)
        self.produtos[self.pid] = livro
        self.pid += 1


    def alterar_livro(self, info):


    def remove_livro():


    def busca_livro(self, info):
