RECOGE LAS MONEDAS
===================

Descripción
-----------
Videojuego de plataformas desarrollado en Python con Pygame Zero.

El objetivo es recoger monedas, evitar enemigos y llegar al cofre después de
alcanzar 50 monedas para conseguir la victoria.


Bibliotecas utilizadas
----------------------
- Pygame Zero
- Random


Requisitos
---------
- Python 3.13
- Pygame Zero


Instalación
---------
1. Instalar Python 3.13.
2. Instalar Pygame Zero:
   python -m pip install pgzero


Ejecución
---------
1. Abrir una terminal.
2. Ubicarse en la carpeta del proyecto.
3. Ejecutar:

       Opción 1: pgzrun juego.py
       Opción 2: python juego.py

La ventana del juego tiene una resolución de 800 x 450 píxeles.


Controles
---------
- A: mover a la izquierda.
- D: mover a la derecha.
- ESPACIO: saltar.
- M: volver al menú después de Game Over o Victoria.


Funcionamiento
--------------
- El jugador comienza con 3 vidas.
- Las monedas aparecen en posiciones aleatorias.
- La dificultad aumenta según la puntuación.
- El primer enemigo aparece desde la parte superior.
- El segundo enemigo aparece al alcanzar 20 monedas.
- El cofre aparece al alcanzar 50 monedas.
- Al tocar el cofre con 50 monedas se obtiene la victoria.
- El juego cuenta con animaciones, música y efectos de sonido.
- El menú permite jugar, activar/desactivar el sonido y salir.
