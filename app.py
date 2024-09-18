from modelos.carros import Carros

carro_fiesta = Carros('Fiesta', 'Ford', 2020, 'Morumbi')
carro_ka = Carros('Ka', 'Ford', 2019, 'Vila A')
carro_onix = Carros('Onix', 'Chevrolet', 2021, 'Centro')

carro_fiesta.alterar_estado()
carro_onix.receber_preço('Concessionária A', 50000)
carro_onix.receber_preço('Concessionária B', 52000)
carro_onix.receber_preço('Concessionária C', 51000)

def main():
    Carros.listar_carros()

if __name__ == '__main__':
    main()
