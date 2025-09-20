from validacion import validacion

def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el elemento [fila{i+1}, columna{j+1}]: "))
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def mostrarMatriz(matriz):
    matriz_str = ""
    for fila in matriz:
        matriz_str += "["
        for elemento in fila:
            matriz_str += f"{elemento:.2f} "
        matriz_str = matriz_str.strip() + "]\n"
    return matriz_str
        
        
        

fila1 = int(input("Ingrese el número de filas de la primera matriz: "))
col1 = int(input("Ingrese el número de columnas de la primera matriz: "))
fila2 = int(input("Ingrese el número de filas de la segunda matriz: "))
col2 = int(input("Ingrese el número de columnas de la segunda matriz: "))



print("Ingrese los elementos de la primera matriz:")
matrizA = crearMatriz(fila1, col1)


print("Ingrese los elementos de la segunda matriz:")
matrizB = crearMatriz(fila2, col2)

op = input("Ingrese la operación a realizar (suma/multiplicacion): ").strip().lower()

# c:\Users\solis\OneDrive\Escritorio\Caculadora matrices\main.py

# ... (código anterior sin cambios)

if op == "suma":
    from suma import validarSuma, sumarMatriz, crearMatrizOperacionesStr, mostrarPasos
    if not validarSuma(matrizA, matrizB):
        print("Error: Las matrices no tienen las mismas dimensiones para la suma.")
    elif not validacion(matrizA) or not validacion(matrizB):
        print("Error: Las matrices contienen elementos no numéricos.")
    else:
        print("\nMatriz A:")
        print(mostrarMatriz(matrizA))
        print("Matriz B:")
        print(mostrarMatriz(matrizB))

        # Paso 1: Mostrar la matriz con las operaciones
        matrizOperaciones = crearMatrizOperacionesStr(matrizA, matrizB)
        print("\nMatriz de operaciones (paso a paso):")
        print(mostrarPasos(matrizOperaciones))
        
        # Paso 2: Calcular y mostrar el resultado final
        resultadoFinal = sumarMatriz(matrizA, matrizB)
        print("Resultado final de la suma:")
        print(mostrarMatriz(resultadoFinal))

# ... (código posterior sin cambios)


