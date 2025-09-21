def validarMultiplicacion(matriz1, matriz2):
    if len(matriz1[0]) != len(matriz2):
        return False
    return True

def multiplicarMatrices(matrizA, matrizB):
    """Realiza la multiplicación numérica y devuelve la matriz resultado."""
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
    Crea una lista de cadenas de texto explicando el cálculo de cada elemento
    de la matriz resultado.
    """
    filasA = len(matrizA)
    columnasA = len(matrizA[0])
    columnasB = len(matrizB[0])
    
    pasosCalculo = []

    for i in range(filasA):
        for j in range(columnasB):
            # Construye la cadena de texto para la operación
            
            operacionStr = ""
            resultadoPaso = 0
            for k in range(columnasA):
                valorA = matrizA[i][k]
                valorB = matrizB[k][j]
                
                operacionStr += f"({valorA:.2f} * {valorB:.2f})"
                if k < columnasA - 1:
                    operacionStr += " + "
                
                resultadoPaso += valorA * valorB

            # Crea la línea completa del paso
            # ej: c1_1 = (2.00 * 1.00) + (3.00 * 5.00) = 17.00
            pasoCompleto = f"C{i+1}, F{j+1} = {operacionStr} = {resultadoPaso:.2f}"
            pasosCalculo.append(pasoCompleto)
            
    return pasosCalculo
