class Restaurante:
    # atributos da classe (compartilhado entre instâncias)
    restaurantes = []

    # construtor com atributos da instância
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    # define a representação em forma de string de um objeto de uma classe
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    # método que itera sobre a lista de restaurantes (atributo da classe) e imprime no terminal os valores
    def listar_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

# instancias da classe
restaurante_praca = Restaurante('Praça', 'Lanches')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.listar_restaurantes() # chama o método que lista os restaurantes que estão guardados na lista restaurantes (atributo da classe)