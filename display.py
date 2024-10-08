import board
import digitalio
import time

# Pines para los segmentos del display (a, b, c, d, e, f, g)
display_pins = (board.GP19, board.GP18, board.GP13, board.GP15, board.GP14, board.GP16, board.GP17)
segments = [digitalio.DigitalInOut(pin) for pin in display_pins]

# Configuraciones para los números
number_3 = [1, 1, 1, 1, 0, 0, 1]  # a, b, c, d, g
number_6 = [0, 1, 1, 1, 1, 1, 1]  # a, f, g, e, d, c
number_8 = [1, 1, 1, 1, 1, 1, 1]  # a, b, c, d, e, f, g

# Configura los pines como salida
for segment in segments:
    segment.direction = digitalio.Direction.OUTPUT

def display_number(number):
    for i, segment in enumerate(segments):
        segment.value = number[i]

# Muestra el número 6
#display_number(number_6)

# Mantener el número mostrado por un tiempo
time.sleep(5)

# Para mostrar el número 3, usa:
display_number(number_3)

# Para mostrar el número 8, usa:
# display_number(number_8)
