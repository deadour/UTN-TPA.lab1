import board
import digitalio
import time

# Configura el pin del sensor Hall (GP0)
hall_sensor = digitalio.DigitalInOut(board.GP1)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = digitalio.Pull.UP  # Resistencia pull-up interna
632

# Configura el LED incorporado (GP25)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("Esperando detección del sensor Hall. Usa CTRL+C para salir.")

try:
    while True:
        if not hall_sensor.value:  # Si el sensor detecta un campo magnético
            print("Sensor Hall activado!")
            led.value = True  # Enciende el LED
            time.sleep(1)     # Mantiene el LED encendido por 1 segundo
            led.value = False  # Apaga el LED
        time.sleep(0.1)  # Espera un poco antes de volver a comprobar
except KeyboardInterrupt:
    pass  # Detiene el programa con Ctrl+C
