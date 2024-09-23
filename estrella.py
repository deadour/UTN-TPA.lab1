import board
import pwmio
import time

def beep(pin, frequency, duration):
    speaker = pwmio.PWMOut(pin, frequency=frequency, duty_cycle=32768)  # Configura el altavoz
    time.sleep(duration)  # Mantiene el sonido durante 'duration' segundos
    speaker.duty_cycle = 0  # Apaga el sonido
    speaker.deinit()  # Libera el pin

# Frecuencias de las notas
C4 = 261  # Do
D4 = 294  # Re
E4 = 329  # Mi
F4 = 349  # Fa
G4 = 392  # Sol
A4 = 440  # La
B4 = 494  # Si

# Melodía de "Estrellita, ¿dónde estás?"
melody = [
    (C4, 0.5), (C4, 0.5), (G4, 0.5), (G4, 0.5),
    (A4, 0.5), (A4, 0.5), (G4, 1.0),
    
    (F4, 0.5), (F4, 0.5), (E4, 0.5), (E4, 0.5),
    (D4, 0.5), (D4, 0.5), (C4, 1.0),
    
    (G4, 0.5), (G4, 0.5), (F4, 0.5), (F4, 0.5),
    (E4, 0.5), (E4, 0.5), (D4, 1.0),
    
    (G4, 0.5), (G4, 0.5), (F4, 0.5), (F4, 0.5),
    (E4, 0.5), (E4, 0.5), (D4, 1.0),
    
    (C4, 0.5), (C4, 0.5), (G4, 0.5), (G4, 0.5),
    (A4, 0.5), (A4, 0.5), (G4, 1.0),
    
    (F4, 0.5), (F4, 0.5), (E4, 0.5), (E4, 0.5),
    (D4, 0.5), (D4, 0.5), (C4, 1.0)
]

# Reproduce la melodía
for note, duration in melody:
    beep(board.GP13, note, duration)
    time.sleep(0.03)  # Breve pausa entre notas
