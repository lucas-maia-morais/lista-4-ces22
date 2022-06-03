class Cliente:
    def __init__(self, info):
        self.id = info.id
        self.lista_produtos  = info.produtos
        self.quantidade = info.quantidade
        self.precos = info.precos

    def produtos(self, dict):
        return [dict[tid] for tid in self.lista_titulos]

    def preco_final(self):
        preco_final = 0
        for p in self.lista_produtos:
            preco_final = self.quantidade[p]*self.precos[p];
        
        return preco_final

    def get_info(self):
        return {
            'produtos': self.produtos(),
            'preco_final': self.preco_final()
        }
