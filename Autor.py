class Autor:
    def __init__(self, info):
        self.id = info.id
        self.nome  = info.nome
        self.email = info.email
        self.lista_titulos = info.titulos

    def titulos(self, dict):
        return [dict[tid] for tid in self.lista_titulos]

    def get_info(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'lista_titulos': self.lista_titulos
        }

