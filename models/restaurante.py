class Restaurante:
    # atributos da classe (compartilhado entre instâncias)
    restaurantes = []

    # construtor com atributos da instância
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)
    
    # define a representação em forma de string de um objeto de uma classe
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # método que itera sobre a lista de restaurantes (atributo da classe) e imprime no terminal os valores
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

# instancias da classe
restaurante_praca = Restaurante('Praça', 'Lanches')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.listar_restaurantes() # chama o método que lista os restaurantes que estão guardados na lista restaurantes (atributo da classe)