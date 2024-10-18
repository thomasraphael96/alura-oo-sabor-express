class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
        
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Lanches'
print(vars(restaurante_praca))

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Express'
restaurante_pizza.categoria = 'Italiano'
print(vars(restaurante_pizza))