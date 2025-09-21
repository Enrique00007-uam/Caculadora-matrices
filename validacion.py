def validacion(Matriz):
    for fila in Matriz:
        for elemento in fila:
            if not isinstance(elemento, (int, float)):
                return False
    return True



