def validarMultiplicacion(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return False
    return True

def multiplicarMatrices(matrizA, matrizB):
    """Hace la multiplicación numérica y devuelve la matriz resultado."""
    filasA = len(matrizA)
    columnasA = len(matrizA[0])
    columnasB = len(matrizB[0])

    matrizResultado = []
    for i in range(filasA):
        filaResultado = []
        for j in range(columnasB):
            suma = 0
            for k in range(columnasA):
                suma += matrizA[i][k] * matrizB[k][j]
            filaResultado.append(suma)
        matrizResultado.append(filaResultado)
    return matrizResultado


def crearPasosMultiplicacion(matrizA, matrizB):
    """
    Hace una lista de texto explicando el cálculo de cada elemento
    de la matriz resultado, incluyendo la suma luego de multiplicar.
    """
    filasA = len(matrizA)
    columnasA = len(matrizA[0])
    columnasB = len(matrizB[0])
    
    pasosCalculo = []

    for i in range(filasA):
        for j in range(columnasB):
            operacionStr = ""
            productosIntermedios = []
            resultadoPaso = 0

            for k in range(columnasA):
                valorA = matrizA[i][k]
                valorB = matrizB[k][j]
                producto = valorA * valorB
                productosIntermedios.append(producto)
                
                operacionStr += f"({valorA:.2f} * {valorB:.2f})"
                if k < columnasA - 1:
                    operacionStr += " + "
                
                resultadoPaso += producto

            sumaStr = " + ".join([f"{p:.2f}" for p in productosIntermedios])

            pasoCompleto = f"F{i+1}, C{j+1} = {operacionStr} -> {sumaStr} = {resultadoPaso:.2f}"
            pasosCalculo.append(pasoCompleto)
            
    return pasosCalculo