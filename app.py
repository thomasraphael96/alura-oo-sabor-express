from models.restaurante import Restaurante

# instancias da classe
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Japa', 'Japonesa')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')

restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes() # chama o método que lista os restaurantes que estão guardados na lista restaurantes (atributo da classe)
    
if __name__ == '__main__':
    main()