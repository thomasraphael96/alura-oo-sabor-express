class Restaurante:
    # construtor
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria}'

restaurante_praca = Restaurante('Praça', 'Lanches')
print(vars(restaurante_praca)) # mostra atributos da instancia
print(dir(restaurante_praca)) # mostra métodos especiais da classe e atributos da classe ou instancia

restaurante_pizza = Restaurante('Pizza Express', 'Italiano')
print(vars(restaurante_pizza))

# antes de definir o método __str__()
print(restaurante_pizza) # saida -> <__main__.Restaurante object at 0x00000270EEFBA090>
# depois de definir o método __str__()
print(restaurante_pizza) #  saida -> Pizza Express | Italiano