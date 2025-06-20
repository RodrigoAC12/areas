"""Módulo principal que ejecuta la aplicación de cálculo de áreas."""

# pylint: disable=no-name-in-module

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from src.vista.ui_main import Ui_MainWindow
from src.logica.areas import Circulo, Triangulo, Rectangulo, Cuadrado


class MainWindow(QMainWindow):
    """Ventana principal de la aplicación."""

    def __init__(self):
        """Inicializa la ventana principal."""
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionSalir.triggered.connect(self.close)
        self.ui.actionCirculo.triggered.connect(self.abrir_dialogo_circulo)
        self.ui.actionTriangulo.triggered.connect(self.abrir_dialogo_triangulo)
        self.ui.actionRectangulo.triggered.connect(self.abrir_dialogo_rectangulo)
        self.ui.actionCuadrado.triggered.connect(self.abrir_dialogo_cuadrado)

    def abrir_dialogo_circulo(self):
        """Abre el diálogo para calcular el área de un círculo."""
        radio, ok = QInputDialog.getDouble(self, "Círculo", "Ingrese el radio:", min=0.01)
        if ok:
            try:
                figura = Circulo(radio)
                area = figura.calcular_area()
                QMessageBox.information(self, "Área Calculada", f"Área del círculo: {area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_triangulo(self):
        """Abre el diálogo para calcular el área de un triángulo."""
        base, ok1 = QInputDialog.getDouble(self, "Triángulo", "Ingrese la base:", min=0.01)
        if not ok1:
            return
        altura, ok2 = QInputDialog.getDouble(self, "Triángulo", "Ingrese la altura:", min=0.01)
        if ok2:
            try:
                figura = Triangulo(base, altura)
                area = figura.calcular_area()
                QMessageBox.information(self, "Área Calculada", f"Área del triángulo: {area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_rectangulo(self):
        """Abre el diálogo para calcular el área de un rectángulo."""
        base, ok1 = QInputDialog.getDouble(self, "Rectángulo", "Ingrese la base:", min=0.01)
        if not ok1:
            return
        altura, ok2 = QInputDialog.getDouble(self, "Rectángulo", "Ingrese la altura:", min=0.01)
        if ok2:
            try:
                figura = Rectangulo(base, altura)
                area = figura.calcular_area()
                QMessageBox.information(self, "Área Calculada", f"Área del rectángulo: {area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))

    def abrir_dialogo_cuadrado(self):
        """Abre el diálogo para calcular el área de un cuadrado."""
        lado, ok = QInputDialog.getDouble(self, "Cuadrado", "Ingrese el lado:", min=0.01)
        if ok:
            try:
                figura = Cuadrado(lado)
                area = figura.calcular_area()
                QMessageBox.information(self, "Área Calculada", f"Área del cuadrado: {area:.2f}")
            except ValueError as e:
                QMessageBox.warning(self, "Error", str(e))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    ventana.show()
    sys.exit(app.exec())
