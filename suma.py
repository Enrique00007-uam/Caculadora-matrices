

def validarSuma(matriz1, matriz2):
    return len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0])

def sumarMatriz(matriz1, matriz2):
    """Realiza la suma numérica y devuelve la matriz resultado."""
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = []
    for i in range(filas):
        filaResultado = []
        for j in range(columnas):
            filaResultado.append(matriz1[i][j] + matriz2[i][j])
        resultado.append(filaResultado)
    return resultado

def crearMatrizOperacionesStr(matriz1, matriz2):
    """Crea una matriz de texto con las operaciones de la suma."""
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    matrizConOperaciones = []
    for i in range(filas):
        filaConOperaciones = []
        for j in range(columnas):
            filaConOperaciones.append(f"{matriz1[i][j]:.2f} + {matriz2[i][j]:.2f}")
        matrizConOperaciones.append(filaConOperaciones)
        
    return matrizConOperaciones

def mostrarPasos(matriz):
    """Muestra una matriz de texto de forma alineada y legible."""
    longitudMaxima = 0
    for fila in matriz:
        for elemento in fila:
            if len(str(elemento)) > longitudMaxima:
                longitudMaxima = len(str(elemento))

    matrizComoTexto = ""
    for fila in matriz:
        matrizComoTexto += "["
        for elemento in fila:
            matrizComoTexto += f"{str(elemento):<{longitudMaxima}}   "
        matrizComoTexto = matrizComoTexto.strip() + "]\n"
    return matrizComoTexto