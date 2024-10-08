import board
import pwmio
import time

def beep(pin, frequency, duration):
    speaker = pwmio.PWMOut(pin, frequency=frequency, duty_cycle=65535)  # Configura el altavoz al máximo
    time.sleep(duration)  # Mantiene el sonido durante 'duration' segundos
    speaker.duty_cycle = 0  # Apaga el sonido
    speaker.deinit()  # Libera el pin

# Frecuencia alta para un sonido molesto
high_frequency = 420  # 2000 Hz

# Reproduce el sonido molesto
try:
    while True:
        beep(board.GP2, high_frequency, 0.5)  # Sonido durante 0.5 segundos
        time.sleep(0.1)  # Breve pausa entre sonidos
except KeyboardInterrupt:
    pass  # Detiene el sonido con Ctrl+C
