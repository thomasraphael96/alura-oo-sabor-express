class Restaurante:
    # atributos da classe (compartilhado entre instâncias)
    restaurantes = []

    # construtor com atributos da instância
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)
    
    # define a representação em forma de string de um objeto de uma classe
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    # método que itera sobre a lista de restaurantes (atributo da classe) e imprime no terminal os valores
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo
        return self._ativo