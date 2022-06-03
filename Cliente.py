class Cliente:
    def __init__(self, info):
        self.id = info.id
        self.nome  = info.nome
        self.email = info.email
        self.compras_passadas = info.compras_passadas

    def compras(self, dict):
        return [dict[tid] for tid in self.lista_titulos]

    def get_info(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'compras_passadas': self.compras()
        }
