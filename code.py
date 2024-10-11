import board
import analogio
import digitalio
import pwmio
import time

#CONFIGURACIÓN--------------------------------------------

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


# Pines para los segmentos del display (a, b, c, d, e, f, g)
display_pins = (board.GP19, board.GP18, board.GP13, board.GP15, board.GP14, board.GP16, board.GP17)
segments = [digitalio.DigitalInOut(pin) for pin in display_pins]

# Configuraciones para los números
number_0 = [1, 1, 0, 1, 1, 1, 1]  # a, b, d, e, f, g
number_1 = [0, 1, 0, 1, 0, 0, 0]  # b, d
number_2 = [1, 1, 1, 0, 0, 1, 1]  # a, b, c, f, g
number_3 = [1, 1, 1, 1, 0, 0, 1]  # a, b, c, d, g
number_4 = [0, 1, 1, 1, 1, 0, 0]  # b, c, d, e
number_5 = [1, 0, 1, 1, 1, 0, 1]  # a, c, d, e, g

#
def select_number(n):
    if n == 1:
        return number_1
    elif n == 2:
        return number_2
    elif n == 3:
        return number_3
    elif n == 4:
        return number_4
    elif n == 5:
        return number_5
    else:
        return number_0
    
    
# Configura los pines como salida
for segment in segments:
    segment.direction = digitalio.Direction.OUTPUT

def display_number(number):
    for i, segment in enumerate(segments):
        segment.value = number[i]

# Funcion para hacer sonar la bocina
def beep(pin, frequency, duration):
    speaker = pwmio.PWMOut(pin, frequency=frequency, duty_cycle=65535)  # Configura el altavoz al máximo
    time.sleep(duration)  # Mantiene el sonido durante 'duration' segundos
    speaker.duty_cycle = 0  # Apaga el sonido
    speaker.deinit()  # Libera el pin

# Variables
screw_deficient= 0
screw_lowV = 0
lastValue = 0
high_frequency = 420  # 2000 Hz
other_frequency = 800
#---------------------------------------------------------
print("Leyendo valores del sensor Hall. Usa CTRL+C para salir.")

try:
    display_number(number_0)
    while True:
        sensor_value = read_sensor(hall_sensor)   #El sensor lee los valores
        
        
        if is_value_valid(sensor_value):    #Verifica que es valido
            if (lastValue - 1000) > sensor_value:     #Pregunta si el valor medido es menor que el anterior (o sea, si el destornillador ya pasó) 
            
            voltage = (lastValue / 65535) * 3.3  # Convertir a voltios
            print(f"El valor promedio del destornillador es: {lastValue}, Voltaje: {voltage:.2f} V")
            
            if voltage<1:
            screw_lowV = screw_lowV + 1 
            screw_deficient= screw_deficient +1
            display_number(select_number(screw_deficient))
            else:
                if voltage>2,5:
                screw_deficient= screw_deficient +1
                display_number(select_number(screw_deficient))
            
            if screw_lowV = 3 or screw_deficient = 5:
                #suena la alarma
                if screw_deficient = 5:
                    for i in range(5):
                        beep(board.GP2, high_frequency, 0,5)  # Sonido durante 0.5 segundos
                        time.sleep(0.1)  # Breve pausa entre sonidos
                else:
                    for i in range(3):
                        beep(board.GP2, other_frequency, 0,5)  # Sonido durante 0.5 segundos
                        time.sleep(0.1)  # Breve pausa entre sonidos
                
                screw_lowV = 0
                screw_deficient = 0
                display_number(number_0)
            
            else:
                lastValue = sensor_value
        else:
            print("Sensor desconectado o sin estímulo.")  # Mensaje si el sensor está desconectado

        time.sleep(0.5)  # Espera 0.5 segundos antes de la siguiente lectura
except KeyboardInterrupt:
    print("Detenido por el usuario.")  # Mensaje al detener el programa
