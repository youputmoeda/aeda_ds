class EmptyListException(Exception):
    print("Não existe elementos na lista.")

class InvalidPositionException(Exception):
    print("Posição invalida")

class NoSuchElementException(Exception):
    print("Não existe o elemento pedido")
    