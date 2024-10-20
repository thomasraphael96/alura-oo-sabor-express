class Avaliacao:
    """
    A classe Avaliacao representa a avaliação de um restaurante feita por um cliente,
    contendo o nome do cliente e a nota dada ao restaurante.

    Atributos:
    ----------
    - _cliente: Nome do cliente que fez a avaliação.
    - _nota: Nota atribuída ao restaurante pelo cliente (deve estar entre 1 e 5).
    """
    def __init__(self, cliente, nota):
        """
        Construtor da classe Avaliacao que inicializa uma nova avaliação com o nome do cliente
        e a nota atribuída.

        Parâmetros:
        -----------
        - cliente: Nome do cliente que está avaliando.
        - nota: Nota dada pelo cliente (deve ser um número entre 1 e 5).
        """
        self._cliente = cliente
        self._nota = nota