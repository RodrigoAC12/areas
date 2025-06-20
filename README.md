# 📐 Aplicación de Cálculo de Áreas con PyQt6

Una aplicación de escritorio desarrollada en **Python** con **PyQt6** que permite calcular el área de diferentes figuras geométricas a través de una interfaz gráfica interactiva.

---

## 🎯 Funcionalidades

✅ Cálculo de áreas para:

- Círculo  
- Triángulo  
- Rectángulo  
- Cuadrado

✅ Interfaz gráfica intuitiva (GUI) diseñada con Qt Designer  
✅ Uso de Programación Orientada a Objetos (POO)  
✅ Validación de entradas (no permite valores negativos)  
✅ Compatible con Windows y Linux  

---

## 🗂️ Estructura del proyecto

    ```plaintext
    proyecto/
    ├── src/
    │   ├── logica/
    │   │   └── areas.py               # Clases POO para el cálculo de áreas
    │   ├── vista/
    │   │   ├── main_window.ui         # Interfaz visual diseñada en Qt Designer
    │   │   └── ui_main.py             # Código generado con pyuic6
    ├── app.py                         # Punto de entrada de la aplicación
    ├── requirements.txt               # Requerimientos de Python
    ├── .gitignore                     # Archivos que no se suben a GitHub
    └── README.md                      # Documentación    


--- 
## 🚀 Requisitos

- Python 3.10 o superior
- PyQt6

---

## 🛠️ Instalación

1️⃣ Clona el repositorio:

    git clone https://github.com/RodrigoAC12/areas.git

2️⃣ Clona el repositorio:

    python -m venv .venv

3️⃣  Activar el entorno virtual  

    .venv\Scripts\activate

3️⃣  Instalar las dependencias 

    pip install PyQt6

▶️ Ejecución

    python app.py

    
✍️ Notas adicionales

  * La interfaz visual fue creada con Qt Designer
  * El archivo .ui se convierte en .py usando:
    
        pyuic6 src/vista/main_window.ui -o src/vista/ui_main.py


## 👨‍💻 Autor
## Rodrigo Arce
