class TaxCalculator():
    def calculateTax(self,preco_compra, preco_venda, genero):
        lucro = max(0, preco_venda - preco_compra) # lucro
        tax = 0
        if genero == 'Fantasia':
            tax = self.getTaxFantasia(lucro)
        else:
            tax = self.getTaxOthers(lucro)
        return tax

    def getTaxFantasia(self,lucro):
        return 0.3*lucro

    def getTaxOthers(self,lucro):
        return 0.2*lucro

if __name__ == '__main__':
    
    tax = TaxCalculator()
    print('Imposto para compra a R$ 20,00 e venda a R$ 30,00 do genêro Fantasia:')
    print('R$ {:.2f}'.format(tax.calculateTax(20.0, 30.0, 'Fantasia')))
    print('')

    print('Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Fantasia')
    print('R$ {:.2f}'.format(tax.calculateTax(20, 40, 'Fantasia')))
    print('')

    print('Imposto para compra a R$ 20,00 e venda a R$ 40,00 do genêro Clássicos Brasileiros')
    print('R$ {:.2f}'.format(tax.calculateTax(20, 40, 'Clássicos Brasileiros')))
    print('')
