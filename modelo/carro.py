class Carro:
clientes = []

def __init__(self, nome, servico, horario, pagamento):
self.nome = nome
self.servico = servico
self.horario = horario
self.pagamento = pagamento
Cliente.clientes.append(self)

def __str_(self):
return f'{self.nome} | {self.servico} | {self.horario} | {self.pagamento}'

def listar_cliente():
for cliente in Cliente.clientes:
print(f'{cliente.nome} | {cliente.servico} | {cliente.horario} | {cliente.pagamento}')
cliente_Maria = Cliente('Maria', 'Corte de cabelo', '10:00', 'Dinheiro')
cliente_Fernanda = Cliente('Fernanda', 'Manicure', '14:00', 'Cartão')
cliente_Ana = Cliente('Ana', 'Corte de cabelo', '11:00', 'Dinheiro')

Cliente.listar_cliente()