from models.restaurante import Restaurante

# instancias da classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Japa', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_praca.alternar_estado()

restaurante_praca.receber_avaliacao('Thomas', 5)
restaurante_praca.receber_avaliacao('Evelyn', 2)
restaurante_praca.receber_avaliacao('Marcos', 3)

def main():
    Restaurante.listar_restaurantes() # chama o método que lista os restaurantes que estão guardados na lista restaurantes (atributo da classe)
    
if __name__ == '__main__':
    main()