class Carros:
    carros = []

    def __init__(self, modelo, fabricante, cor, ano):
        self.modelo = modelo
        self.fabricante = fabricante
        self.cor = cor
        self.ano = ano
        self._disponivel = False
        Carros.carros.append(self)

    def __str__(self):
        return f'{self.modelo} | {self.fabricante} | {self.cor} | {self.ano} | {self.disponivel}'

    @staticmethod
    def listar_carros():
        print('')
        print('''
░█████╗░░█████╗░██████╗░██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝
██║░░╚═╝███████║██████╔╝██████╔╝██║░░██║╚█████╗░
██║░░██╗██╔══██║██╔══██╗██╔══██╗██║░░██║░╚═══██╗
╚█████╔╝██║░░██║██║░░██║██║░░██║╚█████╔╝██████╔╝
░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═════╝░

██████╗░██╗░██████╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███████╗██╗░██████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║██║░░░██║██╔════╝██║██╔════╝
██║░░██║██║╚█████╗░██████╔╝██║░░██║██╔██╗██║██║╚██╗░██╔╝█████╗░░██║╚█████╗░
██║░░██║██║░╚═══██╗██╔═══╝░██║░░██║██║╚████║██║░╚████╔╝░██╔══╝░░██║░╚═══██╗
██████╔╝██║██████╔╝██║░░░░░╚█████╔╝██║░╚███║██║░░╚██╔╝░░███████╗██║██████╔╝
╚═════╝░╚═╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░
''')

        print(f'{"Modelo".ljust(20)} | {"Fabricante".ljust(20)} | {"Cor".ljust(20)} | {"Ano".ljust(20)} | {"Disponível"}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for carro in Carros.carros:
            print(f'{carro.modelo.ljust(20)} | {carro.fabricante.ljust(20)} | {carro.cor.ljust(20)} | {carro.ano.ljust(20)} | {carro.disponivel}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def disponivel(self):
        return '❌ Indisponível' if self._disponivel else '✔️ Disponível'        

# Exemplos de carros
carro_fusca = Carros('Fusca', 'Volkswagen', 'Azul', '1970')
carro_civic = Carros('Civic', 'Honda', 'Preto', '2020')
carro_jetta = Carros('Jetta', 'Volkswagen', 'Branco', '2019')

# Listar carros
Carros.listar_carros()
