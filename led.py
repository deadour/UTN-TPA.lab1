import board
import digitalio
import time

# Configura el LED incorporado (GP25)
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

print("El LED incorporado parpadeará. Usa CTRL+C para salir.")

try:
    while True:
        led.value = True  # Enciende el LED
        time.sleep(0.5)     # Espera 1 segundo
        led.value = False # Apaga el LED
        time.sleep(0.5)     # Espera 1 segundo
except KeyboardInterrupt:
    pass  # Detiene el programa con Ctrl+C
