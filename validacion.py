def validacion(Matriz):
    for fila in Matriz:
        for elemento in fila:
            if not isinstance(elemento, (int, float)):
                return False
    return True


def validarMultiplicacion(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return False
    return True

