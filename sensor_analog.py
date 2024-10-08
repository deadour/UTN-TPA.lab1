import board
import analogio
import time

# Configura el pin del sensor Hall (GP28)
hall_sensor = analogio.AnalogIn(board.GP28)

def read_sensor(sensor, num_samples=5):
    total = 0
    for _ in range(num_samples):
        total += sensor.value
        time.sleep(0.1)  # Espera un poco entre muestras
    return total // num_samples  # Retorna el promedio

def is_value_valid(value, threshold=5000):
    """Verifica si el valor es mayor que un umbral mínimo para considerar que el sensor está conectado."""
    return value > threshold

print("Leyendo valores del sensor Hall. Usa CTRL+C para salir.")

try:
    while True:
        sensor_value = read_sensor(hall_sensor)
        
        if is_value_valid(sensor_value):
            voltage = (sensor_value / 65535) * 3.3  # Convertir a voltios
            print(f"Valor promedio del sensor Hall: {sensor_value}, Voltaje: {voltage:.2f} V")
        else:
            print("Sensor desconectado o sin estímulo.")  # Mensaje si el sensor está desconectado

        time.sleep(0.5)  # Espera 0.5 segundos antes de la siguiente lectura
except KeyboardInterrupt:
    print("Detenido por el usuario.")  # Mensaje al detener el programa
