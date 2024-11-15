import serial
import requests

# Configura el puerto serial
SERIAL_PORT = '/dev/ttyACM1' # Reemplaza 'COM3' con el puerto adecuado para tu sistema
BAUD_RATE = 9600

# URL para la petición HTTP POST
POST_URL = 'https://notificaciones-electronica.vercel.app/api/send-notification'

# Conexión al puerto serial
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Conectado al puerto serial {SERIAL_PORT}")
except serial.SerialException:
    print(f"Error: No se pudo conectar al puerto serial {SERIAL_PORT}")
    exit()

# Bucle principal para leer el puerto serial
def main():
    while True:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == "BUZZER_ACTIVATED":
                send_notification()

# Función para enviar la notificación
def send_notification():
    headers = {'Content-Type': 'application/json'}
    data = {'message': 'Buzzer activado - objeto detectado a menos de 25 cm'}
    try:
        response = requests.post(POST_URL, json=data, headers=headers)\
        
        print(response)

        if response.status_code == 200:
            print("Notificación enviada correctamente")
        else:
            print(f"Error al enviar la notificación: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error en la petición HTTP: {e}")

if __name__ == "__main__":
    main()
