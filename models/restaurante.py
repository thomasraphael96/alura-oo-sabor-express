class Restaurante:
    # construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

restaurante_praca = Restaurante('Praça', 'Lanches')
print(vars(restaurante_praca))
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')
print(vars(restaurante_pizza))