

# Laboratorio N° 1 - Tecnologías para la Automatización

Este trabajo de laboratorio consiste en poner en práctica los conceptos de la materia y utilizar un Microprocesador modelo Raspberry Pico W 2022, junto con sensores específicos y un código utilizando CircuitPython para interactuar con objetos de la realidad. En este caso, el grupo posee un sensor de efecto Hall (detector de campo magnético), una bocina y un display de 7 segmentos. La idea es crear un escenario ficticio que se adapte a estos componentes, de manera tal que permitan resolver un problema de la vida real.

## Componentes del Sistema
- Microcontrolador RP2-B2 (Raspberry Pi Pico W)
- Sensor de Efecto Hall 49E (920BD)
- Imán.
- Display de 7 Segmentos.
- Bocina.
- Protoboard y Set de Cables.




## Alumnos:
- Aguirre, Amilcar
- Neira, Nicolás
- Stegmayer, Tobías
- Ramírez, Eduardo


## Descripción del Escenario
En una fábrica de herramientas, específicamente en la línea de producción de destornilladores, es esencial asegurar que cada destornillador esté magnetizado adecuadamente para cumplir con los estándares de calidad. Un sistema automatizado se implementa para verificar la magnetización de los destornilladores utilizando un sensor de efecto Hall. Este sistema no solo mide la magnetización, sino que también gestiona alertas y lleva un registro de los destornilladores que no cumplen con los estándares.

## Funcionamiento del Sistema
El sistema está diseñado para operar de manera continua y automática, asegurando que cada destornillador que pase por la línea de producción esté adecuadamente magnetizado. Posee las siguientes funciones:

### Detección de Magnetización:
El sensor de efecto Hall, un dispositivo que mide campos magnéticos, está posicionado estratégicamente para evaluar cada destornillador y toma muestra cada dos segundos.
Normalmente, el sensor emite un voltaje de aproximadamente 1.68 voltios cuando no hay un campo magnético presente.
Cuando un destornillador pasa bajo el sensor, si el voltaje sube hacia 2.10 voltios (lo máximo registrado en una muestra) o baja hacia 0.90 voltios (lo mínimo registrado), significa que el destornillador está fuera del rango de magnetización adecuado.

### Contador de Defectos:
Cada vez que el voltaje excede 1.76 voltios o cae por debajo de 1.60 voltios, el sistema incrementa un contador de defectos.
Este contador se muestra en un display de 7 segmentos, permitiendo al personal de la fábrica ver rápidamente cuántos destornilladores no cumplen con los estándares.

### Alarma de Producción:
Si el contador alcanza 5, es decir, si cinco destornilladores consecutivos están fuera del rango adecuado, la bocina suena 5 veces. Esto alerta al equipo de producción de un posible problema en la línea.

### Alarma de Magnetización Baja:
Si se detectan tres destornilladores consecutivos con voltaje por debajo de 1.60 voltios, el sistema emite una alerta sonora distinta 3 veces, indicando un problema específico de magnetización baja.

### Reseteo del Contador:
Cada vez que suena una alarma, el contador se resetea automáticamente, permitiendo que el sistema comience a contar desde cero nuevamente.

### Implementación Técnica
Programación: Utilizamos CircuitPython en la Raspberry Pi Pico W para programar todo el sistema. 



## Códigos:

- led.py : prende la luz led incoporada del Microprocesador
- bocina.py : reproduce un sonido en la bocina. Es utilizado para pruebas.
- estrella.py reproduce el sonido de la canción 'Estrellita donde estás' en el speaker. Inicialmente, fue creado y usado para pruebas.
- sensor_analog.py activa el sensor Hall 49E y toma muestras cada 0.1 segundos del campo magnético, y calcula el voltaje producido.
- code.py deberia sincronizar todos los componentes en base al escenario.

