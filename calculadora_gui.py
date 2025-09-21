import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QGroupBox, QGridLayout, QSpinBox, QPushButton,
    QTableWidget, QTableWidgetItem, QTextEdit, QMessageBox, QHeaderView
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

# Reutilizamos la lógica de los archivos existentes
from suma import validarSuma, sumarMatriz, crearMatrizOperacionesStr
# Importamos la nueva lógica de multiplicación
from multiplicacion import multiplicarMatrices, crearPasosMultiplicacion, validarMultiplicacion

class CalculadoraMatricesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Matrices")
        self.setGeometry(100, 100, 800, 700)

        # Widget principal y layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QVBoxLayout(self.central_widget)
        self.layout_principal.setSpacing(15)
        self.layout_principal.setContentsMargins(20, 20, 20, 20)
        
        self.initUI()

    def initUI(self):
        # 1. Banner
        self.crear_banner()

        # 2. Sección de entrada de matrices
        layout_matrices = QHBoxLayout()
        self.grupo_matriz_a = self.crear_grupo_matriz("Primera Matriz", "A")
        self.grupo_matriz_b = self.crear_grupo_matriz("Segunda Matriz", "B")
        layout_matrices.addWidget(self.grupo_matriz_a)
        layout_matrices.addWidget(self.grupo_matriz_b)
        self.layout_principal.addLayout(layout_matrices)

        # 3. Botones de operación
        self.crear_botones_operacion()

        # 4. Pizarra de resultados
        self.crear_pizarra_resultados()

    def crear_banner(self):
        banner = QLabel("Calculadora de Matrices")
        banner.setFont(QFont("Arial", 20, QFont.Weight.Bold))
        banner.setAlignment(Qt.AlignmentFlag.AlignCenter)
        banner.setStyleSheet("background-color: #89CFF0; color: black; padding: 10px; border-radius: 5px; font-size: 18px;")
        self.layout_principal.addWidget(banner)

    def crear_grupo_matriz(self, titulo, id_matriz):
        grupo = QGroupBox(titulo)
        layout_grupo = QVBoxLayout(grupo)

        # Controles para dimensiones
        layout_dimensiones = QHBoxLayout()
        layout_dimensiones.addWidget(QLabel("Filas:"))
        spin_filas = QSpinBox()
        spin_filas.setMinimum(1)
        spin_filas.setValue(2)
        layout_dimensiones.addWidget(spin_filas)

        layout_dimensiones.addWidget(QLabel("Columnas:"))
        spin_columnas = QSpinBox()
        spin_columnas.setMinimum(1)
        spin_columnas.setValue(2)
        layout_dimensiones.addWidget(spin_columnas)
        
        btn_crear = QPushButton("Crear/Actualizar Matriz")
        btn_crear.setStyleSheet("padding: 5px;")
        layout_dimensiones.addWidget(btn_crear)
        
        layout_grupo.addLayout(layout_dimensiones)

        # Tabla para la matriz
        tabla = QTableWidget(2, 2)
        tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        tabla.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout_grupo.addWidget(tabla)

        # Conectar señal del botón
        btn_crear.clicked.connect(lambda: self.actualizar_tabla_matriz(
            spin_filas.value(), spin_columnas.value(), tabla
        ))

        # Guardar referencias
        if id_matriz == 'A':
            self.spin_filas_a = spin_filas
            self.spin_columnas_a = spin_columnas
            self.tabla_matriz_a = tabla
        else:
            self.spin_filas_b = spin_filas
            self.spin_columnas_b = spin_columnas
            self.tabla_matriz_b = tabla
            
        return grupo

    def actualizar_tabla_matriz(self, filas, columnas, tabla):
        tabla.setRowCount(filas)
        tabla.setColumnCount(columnas)

    def crear_botones_operacion(self):
        layout_botones = QHBoxLayout()
        layout_botones.setSpacing(10)

        btn_sumar = QPushButton("Sumar matrices")
        btn_multiplicar = QPushButton("Multiplicar matrices")
        btn_limpiar = QPushButton("limpiar")

        estilo_boton = """
            QPushButton {
                background-color: #89CFF0;
                color: black;
                border: none;
                padding: 10px 20px;
                font-size: 15px;
                border-radius: 15px;
               
            }
            QPushButton:hover {
                background-color: #7AC5E0;
            }
            QPushButton:pressed {
                background-color: #69B4D0;
            }
        """

        for btn in [btn_sumar, btn_multiplicar, btn_limpiar]:
            btn.setStyleSheet(estilo_boton)
            layout_botones.addWidget(btn)

        self.layout_principal.addLayout(layout_botones)

        # Conectar señales
        btn_sumar.clicked.connect(self.realizar_suma)
        btn_multiplicar.clicked.connect(self.realizar_multiplicacion) # Actualizado
        btn_limpiar.clicked.connect(self.limpiar_todo)

    def crear_pizarra_resultados(self):
        grupo_pizarra = QGroupBox("Pizarra de Resultados")
        layout_pizarra = QVBoxLayout(grupo_pizarra)
        
        self.pizarra = QTextEdit()
        self.pizarra.setReadOnly(True)
        self.pizarra.setFont(QFont("Courier New", 14))
        self.pizarra.setStyleSheet("background-color: white; color: black;")
        
        layout_pizarra.addWidget(self.pizarra)
        self.layout_principal.addWidget(grupo_pizarra)

    def leer_matriz_desde_tabla(self, tabla):
        filas = tabla.rowCount()
        columnas = tabla.columnCount()
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                item = tabla.item(i, j)
                if item and item.text():
                    try:
                        valor = float(item.text().replace(',', '.'))
                        fila.append(valor)
                    except ValueError:
                        self.mostrar_error("Valor no numérico", f"El valor en la celda [{i+1}, {j+1}] no es un número válido.")
                        return None
                else:
                    # Asumir 0 si la celda está vacía
                    fila.append(0.0)
            matriz.append(fila)
        return matriz

    def formatear_matriz_html(self, matriz, titulo=""):
        html = f"<h3>{titulo}</h3>"
        html += "<table border='1' style='border-collapse: collapse; margin-bottom: 10px;'>"
        for fila in matriz:
            html += "<tr>"
            for elemento in fila:
                elemento_str = str(elemento)
                html += f"<td style='padding: 5px; text-align: center;'>{elemento_str}</td>"
            html += "</tr>"
        html += "</table>"
        return html

    def realizar_suma(self):
        matriz_a = self.leer_matriz_desde_tabla(self.tabla_matriz_a)
        matriz_b = self.leer_matriz_desde_tabla(self.tabla_matriz_b)

        if matriz_a is None or matriz_b is None:
            return

        if not validarSuma(matriz_a, matriz_b):
            self.mostrar_error("Error de Dimensiones", "Las matrices deben tener las mismas dimensiones para poder sumarse.")
            return
        
        self.pizarra.clear()

        self.pizarra.append(self.formatear_matriz_html(matriz_a, "Matriz A"))
        self.pizarra.append(self.formatear_matriz_html(matriz_b, "Matriz B"))

        matriz_operaciones = crearMatrizOperacionesStr(matriz_a, matriz_b)
        self.pizarra.append(self.formatear_matriz_html(matriz_operaciones, "Pasos intermedios de la suma"))

        resultado = sumarMatriz(matriz_a, matriz_b)
        self.pizarra.append(self.formatear_matriz_html(resultado, "Resultado final de la operación"))

    def realizar_multiplicacion(self):
        matriz_a = self.leer_matriz_desde_tabla(self.tabla_matriz_a)
        matriz_b = self.leer_matriz_desde_tabla(self.tabla_matriz_b)

        if matriz_a is None or matriz_b is None:
            return

        # Usamos la función de validación existente
        if not validarMultiplicacion(matriz_a, matriz_b):
            self.mostrar_error("Error de Dimensiones", 
                               "El número de columnas de la Matriz A debe ser igual al número de filas de la Matriz B.")
            return
        
        self.pizarra.clear()

        # Mostrar matrices originales
        self.pizarra.append(self.formatear_matriz_html(matriz_a, "Matriz A"))
        self.pizarra.append(self.formatear_matriz_html(matriz_b, "Matriz B"))

        # Mostrar pasos del cálculo
        pasos = crearPasosMultiplicacion(matriz_a, matriz_b)
        html_pasos = "<h3>Pasos del Cálculo:</h3>"
        html_pasos += "<br>".join(pasos) # Unimos cada paso con un salto de línea
        self.pizarra.append(html_pasos)

        # Mostrar resultado final
        resultado = multiplicarMatrices(matriz_a, matriz_b)
        self.pizarra.append(self.formatear_matriz_html(resultado, "Resultado Final"))

    def limpiar_todo(self):
        for i in range(self.tabla_matriz_a.rowCount()):
            for j in range(self.tabla_matriz_a.columnCount()):
                self.tabla_matriz_a.setItem(i, j, QTableWidgetItem(""))
        
        for i in range(self.tabla_matriz_b.rowCount()):
            for j in range(self.tabla_matriz_b.columnCount()):
                self.tabla_matriz_b.setItem(i, j, QTableWidgetItem(""))

        self.pizarra.clear()

    def proximamente(self):
        # Esta función ya no es necesaria para la multiplicación
        QMessageBox.information(self, "Próximamente", "Esta funcionalidad se implementará pronto.")

    def mostrar_error(self, titulo, mensaje):
        QMessageBox.critical(self, titulo, mensaje)

# c:\Users\solis\OneDrive\Escritorio\Caculadora matrices\calculadora_gui.py

# ... (código anterior sin cambios)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Estilo global para un modo claro y moderno con texto negro
    app.setStyleSheet("""
    QWidget { color: black; }
        QMainWindow, QWidget {
            background-color: #f0f0f0;
        }
        QGroupBox {
            font-size: 14px;
            font-weight: bold;
            border: 1px solid #d0d0d0;
            border-radius: 8px;
            margin-top: 10px;
            background-color: #fafafa;
            color: black; /* Título del grupo en negro */
        }
        QGroupBox::title {
            subcontrol-origin: margin;
            subcontrol-position: top left;
            padding: 0 5px;
            background-color: #fafafa;
            border-radius: 4px;
        }
        QLabel {
            color: black; /* Texto negro para máxima legibilidad */
            font-size: 13px;
        }
        QSpinBox, QTableWidget {
            background-color: white;
            color: black;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        QHeaderView::section {
            background-color: #e8e8e8;
            padding: 4px;
            border: 1px solid #d0d0d0;
            color: black; /* Texto de la cabecera en negro */
        }
    """)

    ventana = CalculadoraMatricesApp()
    ventana.show()
    sys.exit(app.exec())
