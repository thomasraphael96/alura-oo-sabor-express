import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.avaliacao import Avaliacao
from models.item_cardapio import ItemCardapio

class Restaurante:
    """
    A classe Restaurante representa um estabelecimento que pode receber avaliações de clientes,
    alternar entre os estados "ativo" e "inativo", e listar todos os restaurantes criados.

    Atributos da classe:
    --------------------
    - restaurantes: Lista que armazena todas as instâncias de Restaurante criadas.

    Atributos da instância:
    -----------------------
    - _nome: Nome do restaurante (formatado com a primeira letra de cada palavra em maiúscula).
    - _categoria: Categoria do restaurante (armazenado em letras maiúsculas).
    - _ativo: Estado atual do restaurante, indicando se ele está ativo ou não (padrão: False).
    - _avaliacoes: Lista de avaliações recebidas pelo restaurante.
    """
    restaurantes = []

    # construtor com atributos da instância
    def __init__(self, nome, categoria):
        """
        Construtor da classe Restaurante, que inicializa uma nova instância com nome, categoria,
        status ativo/inativo e uma lista de avaliações vazia.

        Parâmetros:
        -----------
        - nome: Nome do restaurante.
        - categoria: Categoria do restaurante.
        """
        self._nome = nome.title() # Formata o nome com a primeira letra maiúscula
        self._categoria = categoria.upper() # Armazena a categoria em letras maiúsculas
        self._ativo = False # Estado inicial do restaurante
        self._avaliacoes = [] # Lista de avaliações
        self._cardapio = [] # Lista de itens do cardápio
        Restaurante.restaurantes.append(self) # Adiciona o restaurante à lista da classe
    
    # define a representação em forma de string de um objeto de uma classe
    def __str__(self):
        """
        Retorna uma string representando o restaurante no formato 'Nome | Categoria'.
        """
        return f'{self._nome} | {self.categoria}'
    
    # método que itera sobre a lista de restaurantes (atributo da classe) e imprime no terminal os valores
    @classmethod
    def listar_restaurantes(cls):
        """
        Método de classe que lista todos os restaurantes criados, mostrando o nome, a categoria,
        a média de avaliações e o status de cada um. A tabela é impressa no terminal.
        """
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    @property
    def ativo(self):
        """
        Retorna uma representação visual do status do restaurante:
        - '☑' se ativo.
        - '☐' se inativo.
        """
        return '☑' if self._ativo else '☐'

    def alternar_estado(self):
        """
        Alterna o estado do restaurante entre ativo e inativo.

        Retorna:
        --------
        - O novo estado (True se ativo, False se inativo).
        """
        self._ativo = not self._ativo
        return self._ativo
    
    def receber_avaliacao(self, cliente, nota):
        """
        Recebe uma nova avaliação de um cliente, com uma nota de 1 a 5.

        Parâmetros:
        -----------
        - cliente: Nome do cliente que está avaliando.
        - nota: Nota dada pelo cliente (deve estar entre 1 e 5).
        """
        if 0 < nota <= 5: 
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)
        else:
            print('Dê uma nota entre 1 e 5.')
    
    @property
    def media_avaliacoes(self):
        """
        Calcula e retorna a média das avaliações do restaurante.

        Retorna:
        --------
        - A média das notas das avaliações ou '-' se não houver avaliações.
        """
        if not self._avaliacoes:
            return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        quantidade_de_notas = len(self._avaliacoes)
        media_das_notas = round(soma_das_notas / quantidade_de_notas, 1)
        return media_das_notas
    
    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardario(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Descrição: {item.descricao}'
            else:
                mensagem = f'{i}. Nome: {item._nome} | Preço: R${item._preco:.2f} | Tamanho: {item.tamanho}'
            print(mensagem)