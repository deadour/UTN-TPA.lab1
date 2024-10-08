import board
import pwmio
import time

# Inicializa PWM para cada canal de color del LED RGB
red = pwmio.PWMOut(board.GP26, frequency=1000, duty_cycle=0)  # Canal rojo en GP26
green = pwmio.PWMOut(board.GP22, frequency=1000, duty_cycle=0)  # Canal verde en GP22
blue = pwmio.PWMOut(board.GP28, frequency=1000, duty_cycle=0)  # Canal azul en GP28

# Función para establecer el color del LED RGB
def set_color(r, g, b):
    red.duty_cycle = r  # Intensidad roja
    green.duty_cycle = g  # Intensidad verde
    blue.duty_cycle = b  # Intensidad azul

try:
    while True:
        set_color(65535, 0, 0)  # Rojo
        time.sleep(2)
        set_color(0, 65535, 0)  # Verde
        time.sleep(2)
        set_color(0, 0, 65535)  # Azul
        time.sleep(2)
except KeyboardInterrupt:
    set_color(0, 0, 0)  # Apagar el LED RGB en interrupción
