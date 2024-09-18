from modelos.valor import Valor

class Carros:
    carros = []

    def __init__(self, modelo, fabricante, ano, local):
        self._modelo = modelo.upper()
        self._fabricante = fabricante.title()
        self._ano = ano
        self._local = local.title()
        self._disponivel = True
        self._valor = []
        Carros.carros.append(self)

    def __str__(self):
        return f'{self._modelo} | {self._fabricante} | {self._ano} | {self._local} | {self._disponivel}'

    @classmethod
    def listar_carros(cls):
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
        
        print(f'{"Modelo".ljust(20)} | {"Fabricante".ljust(20)} | {"Ano".ljust(20)} | {"Local".ljust(20)} | {"Disponível".ljust(20)} | {"Média Preço".ljust(20)}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for carro in cls.carros:
            print(f'{carro._modelo.ljust(20)} | {carro._fabricante.ljust(20)} | {str(carro._ano).ljust(20)} | {carro._local.ljust(20)} | {carro.disponivel.ljust(20)} | {carro.media_preço}')
            print('------------------------------------------------------------------------------------------------------------------------------')

    @property
    def disponivel(self):
        return '❌ Indisponível' if not self._disponivel else '✔️ Disponível'

    def alterar_estado(self):
        self._disponivel = not self._disponivel        

    def receber_preço(self, concessionaria, preço):
        preço = Valor(concessionaria, preço)
        self._valor.append(preço)

    @property
    def media_preço(self):
        if not self._valor:
            return 0 
        somas_dos_preços = sum(valor._preço for valor in self._valor)
        quantidade_concessionaria = len(self._valor)
        media = round(somas_dos_preços / quantidade_concessionaria, 1)
        return media



