import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.avaliacao import Avaliacao

class Restaurante:
    # atributos da classe (compartilhado entre instâncias)
    restaurantes = []

    # construtor com atributos da instância
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)
    
    # define a representação em forma de string de um objeto de uma classe
    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    # método que itera sobre a lista de restaurantes (atributo da classe) e imprime no terminal os valores
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        self._ativo = not self._ativo
        return self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print('Dê uma nota entre 1 e 5.')
    
    @property
    def media_avaliacoes(self):
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas