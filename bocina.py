import board
import pwmio
import time
import digitalio

def beep(pin, frequency, duration):
    speaker = pwmio.PWMOut(pin, frequency=frequency, duty_cycle=65535)  # Configura el altavoz al máximo
    time.sleep(duration)  # Mantiene el sonido durante 'duration' segundos
    speaker.duty_cycle = 0  # Apaga el sonido
    speaker.deinit()  # Libera el pin

# Configura el pin del sensor Hall
hall_sensor_pin = board.GP0  # Cambia esto al pin que estés usando
hall_sensor = digitalio.DigitalInOut(hall_sensor_pin)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = digitalio.Pull.UP  # Activa la resistencia pull-up interna

# Frecuencia para el sonido molesto
high_frequency = 420  # Frecuencia en Hz

try:
    while True:
        if not hall_sensor.value:  # Detecta el estado bajo (cuando el imán está cerca)
            print("Sensor Hall activado!")
            beep(board.GP13, high_frequency, 0.5)  # Reproduce sonido
        else:
            print("Sensor Hall inactivo.")
        time.sleep(0.1)  # Espera un poco antes de volver a comprobar
except KeyboardInterrupt:
    pass  # Detiene el programa con Ctrl+C
