from models.restaurante import Restaurante
from models.bebida import Bebida
from models.prato import Prato

# instancias da classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Japa', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

# alternando estado para ativo
restaurante_praca.alternar_estado()

# avaliações
restaurante_praca.receber_avaliacao('Thomas', 5)
restaurante_praca.receber_avaliacao('Evelyn', 2)
restaurante_praca.receber_avaliacao('Marcos', 3)

# criando itens do cardápio
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
prato_paozinho = Prato('Pãozinho', 2.0, 'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)

def main():
    # Restaurante.listar_restaurantes() # chama o método que lista os restaurantes que estão guardados na lista restaurantes (atributo da classe)
    print(bebida_suco)
    print(prato_paozinho)
    
if __name__ == '__main__':
    main()