import board
import digitalio
import time

# Configura el LED integrado
try:
    led = digitalio.DigitalInOut(board.LED)  
except AttributeError:
    led = digitalio.DigitalInOut(board.GP25)  

led.direction = digitalio.Direction.OUTPUT

#pin del sensor Hall 
hall_sensor = digitalio.DigitalInOut(board.GP0)
hall_sensor.direction = digitalio.Direction.INPUT
hall_sensor.pull = digitalio.Pull.UP  # activa la resistencia pull-up interna

try:
    while True:
        if not hall_sensor.value:  # Detecta el estado bajo (cuando el imán está cerca)
            print("Sensor Hall activado! Encendiendo LED.")
            led.value = True  # enciende el LED
        else:
            print("Sensor Hall inactivo. Apagando LED.")
            led.value = False  # apaga el LED
        time.sleep(0.1)  # Espera antes de volver a comprobar
except KeyboardInterrupt:
    pass  # Detiene el programa con Ctrl+C
