class Livro:
    def __init__(self, info):
        self.id = info.id
        self.titulo = info.titulo
        self.autor = info.autor
        self.genero = info.genero
        self.edicao = info.edicao
        self.editora = info.editora
        self.preco_venda = info.preco_venda
        self.preco_compra = info.preco_compra
        self.estoque = self.estoque
    
    def impostos(self):
        lucro = max(0, self.preco_venda - self.preco_compra) # lucro
        pimp_genero = 0.2 # porcentagem padrão de imposto sobre lucro para qualquer genero
        if self.genero == 'Fantasia':
            pimp_genero = 0.3 # % imposto sobre livros de fantasia
        return lucro*pimp_genero

    def get_info(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'genero': self.genero,
            'edicao': self.edicao,
            'editora': self.editora,
            'preco_venda': self.preco_venda,
            'preco_compra': self.preco_compra,
            'self.estoque': self.estoque,
            'self.imposot': self.impostos()
        }
            
