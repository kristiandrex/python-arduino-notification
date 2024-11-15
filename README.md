# Notificaciones con Sensor y Arduino

Este proyecto utiliza Python para leer datos desde un puerto serial conectado a un Arduino y envía notificaciones HTTP cuando se reciba el evento `BUZZER_ACTIVATED`

## Requisitos
- Python 3.8 o superior
- Entorno virtual `venv`
- Arduino conectado al puerto serial
- Dependencias: `pyserial`, `requests`

## Instalación

### Windows

1. **Clonar el repositorio**:
   ```cmd
   git clone https://github.com/kristiandrex/python-arduino-notification
   cd python-arduino-notification
   ```

2. **Crear el entorno virtual**:
   ```cmd
   python -m venv venv
   .\venv\Scripts\activate.bat
   ```

3. **Instalar dependencias**:
   ```cmd
   pip install -r requirements.txt
   ```

4. **Configurar el puerto serial**:
   Editar el archivo `main.py` y reemplazar la línea:
   ```python
   SERIAL_PORT = '/dev/ttyACM1'
   ```
   con el puerto adecuado, por ejemplo:
   ```python
   SERIAL_PORT = 'COM3'
   ```

### Linux

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/kristiandrex/python-arduino-notification
   cd python-arduino-notification
   ```

2. **Crear el entorno virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar el puerto serial**:
   Editar el archivo `main.py` y asegurarse de que `SERIAL_PORT` esté configurado correctamente, por ejemplo:
   ```python
   SERIAL_PORT = '/dev/ttyACM1'
   ```

## Ejecución

1. Activar el entorno virtual:

   **Windows**:
   ```cmd
   .\venv\Scripts\activate.bat
   ```

   **Linux**:
   ```bash
   source venv/bin/activate
   ```

2. Ejecutar el script principal:
   ```bash
   python main.py
   ```
