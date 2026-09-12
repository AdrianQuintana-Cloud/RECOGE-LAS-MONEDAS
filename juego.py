import pgzrun
import random

WIDTH = 800
HEIGHT = 450

# ESTADO DEL JUEGO
game_started = False
game_over = False
game_won = False

# SONIDOS
sound_enable = True
music_volume = 0.5

def play_sound(sound):

    if sound_enable:
        sound.play()

def update_music():

    if sound_enable:
        music.play("ambient")
        music.set_volume(music_volume)

    else:
        music.stop()

# BOTONES DEL MENU
play_button = Actor("play_button")
play_button.pos = (WIDTH // 2 - 200, 360)

sound_button = Actor("sound_on")
sound_button.pos = (WIDTH // 2, 360)

exit_button = Actor("exit_button")
exit_button.pos = (WIDTH // 2 + 200, 360)

# PERSONAJE
player = Actor("player0")
player.pos = (400, 350)

# ANIMACION DEL JUGADOR
player_frames_r = ["player0", "player1", "player2", "player3", "player4", "player5", "player6", "player7"]
player_frames_l = ["playerl0", "playerl1", "playerl2", "playerl3", "playerl4", "playerl5", "playerl6", "playerl7"]
player_frame = 0
player_animation_timer = 0
player_animation_speed = 5
player_fancing_left = False

# ANIMACION EN REPOSO DEL JUGADOR
player_idle_frames_r = ["player0", "player8"]
player_idle_frames_l = ["playerl0", "playerl8"]
player_idle_frame = 0
player_idle_timer = 0
player_idle_speed = 15

def animate_actor(actor, frames, frame_index):
    actor.image = frames[frame_index]

# MONEDA
coin = Actor("coin3")
coin.pos = (
    random.randint(50, 750), 
    random.randint(50, 350)
    )

# ANIMACION DE LA MONEDA
coin_frames = ["coin0", "coin1", "coin2", "coin3", "coin4", "coin5"]
coin_frame = 0
coin_animation_timer = 0
coin_animation_speed = 6

# COFRE
chest = Actor("chest")
chest.pos = (650, 110)

# PLATAFORMAS
platforms = [
    Rect((0, 410), (800, 40)),
    Rect((100, 320), (100, 20)),
    Rect((600, 320), (100, 20)),
    Rect((350, 240), (100, 20)),
    Rect((100, 150), (100, 20)),
    Rect((600, 150), (100, 20))
]

platform_sprites = []

for platform in platforms[1:]:
    sprite = Actor("platform")
    sprite.center = platform.center
    platform_sprites.append(sprite)

# ENEMIGO 1
enemies = []
enemy_speed = 3
spawn_interval = 120
spawn_timer = 0
max_enemies = 1
difficulty_level = 1
enemy_frames = ["goomba0", "goomba1", "goomba2"]
enemy_animation_speed = 5

# CREACION DE ENEMIGO 1
def create_enemy():

    enemy = Actor("goomba0")
    enemy.pos = (
        random.randint(40, WIDTH - 40),
        -50
    )
    enemy.frame = 0
    enemy.animation_timer = 0
    enemies.append(enemy)

# ENEMIGO 2
turtle = Actor("turtle0")
turtle_speed = 3
turtle_active = False
turtle_frame = 0
turtle_animation_timer = 0
turtle_animation_speed = 5
turtle_frames = ["turtle0", "turtle1", "turtle2", "turtle3", "turtle4", "turtle5", "turtle6", "turtle7"]

# CREACION DE ENEMIGO 2
def create_turtle():

    global turtle_active
    turtle.image = turtle_frames[0]
    turtle.x = WIDTH + turtle.width // 2
    turtle.bottom = platforms[0].top
    turtle_active = True

# GRAVEDAD
gravity = 0.5
velocity_y = 0
jump_strength = -10
on_ground = False

# PUNTUACION Y VIDAS
score = 0
lives = 3

# DIFICULTAD DE JUEGO
def update_difficulty():

    global difficulty_level
    global enemy_speed
    global spawn_interval
    global max_enemies

    if score < 5:
        difficulty_level = 1
        enemy_speed = 3
        spawn_interval = 120
        max_enemies = 1

    elif score < 10:
        difficulty_level = 2
        enemy_speed = 4
        spawn_interval = 100
        max_enemies = 2

    elif score < 20:
        difficulty_level = 3
        enemy_speed = 5
        spawn_interval = 80
        max_enemies = 3

    elif score < 30:
        difficulty_level = 4
        enemy_speed = 6
        spawn_interval = 60
        max_enemies = 4

    else:
        difficulty_level = 5
        enemy_speed = 7
        spawn_interval = 45
        max_enemies = 5

# REINICIO DE PARTIDA
def reset_game():

    global score
    global lives
    global game_over
    global game_won
    global velocity_y
    global on_ground
    global spawn_timer
    global difficulty_level 
    global turtle_active 
    global turtle_animation_timer 

    score = 0
    lives = 3
    game_over = False
    velocity_y = 0
    on_ground = False
    spawn_timer = 0
    difficulty_level = 1
    turtle_active = False
    turtle_animation_timer = 0

    turtle.image = "turtle0"
    enemies.clear()
    player.pos = (400, 350)
    coin.pos = (
        random.randint(50, 750),
        random.randint(50, 350)
    )

    update_difficulty()

# VOLVER AL MENU
def return_to_menu():

    global game_started
    global game_over
    global game_won

    game_started = False
    game_over = False
    game_won = False

    enemies.clear()

    play_button.image = "play_button"
    exit_button.image = "exit_button"

    update_sound_button()
    update_music()

# ACTUALIZAR BOTON DE SONIDO
def update_sound_button():

    if sound_enable:
        sound_button.image = "sound_on"
    else:
        sound_button.image = "sound_off"

def draw():

    # PANTALLA DE INICIO
    if not game_started:

        screen.blit("background", (0, 0))

        screen.draw.text(
            "RECOGE LAS MONEDAS",
            center = (WIDTH // 2, 70),
            fontname = "pixel",
            fontsize = 35,
            color = "black"
        )

        screen.draw.text(
            "A / D para moverte",
            center = (WIDTH // 2, 150),
            fontname = "pixel",
            fontsize = 20,
            color = "white"
        )

        screen.draw.text(
            "ESPACIO para saltar",
            center = (WIDTH // 2, 180),
            fontname = "pixel",
            fontsize = 20,
            color = "white"
        )

        screen.draw.text(
            "RECOGE las 50 monedas y",
            center = (WIDTH // 2, 240),
            fontname = "pixel",
            fontsize = 20,
            color = "white"
        )

        screen.draw.text(
            "EVITA a los enemigo",
            center = (WIDTH // 2, 270),
            fontname = "pixel",
            fontsize = 20,
            color = "white"
        )

        play_button.draw()
        sound_button.draw()
        exit_button.draw()

        return

    # JUEGO
    screen.blit("background_game", (0, 0))

    for platform_sprite in platform_sprites:
        platform_sprite.draw()

    # PERSONAJES
    player.draw()
    coin.draw()

    if score >= 50 and not game_won:
        chest.draw()

    for enemy in enemies:
        enemy.draw()

    if turtle_active:
        turtle.draw()

    # INFORMACION
    screen.draw.text(
        "Vidas: " + str(lives),
        (50, 20),
        fontname = "pixel",
        fontsize = 18,
        color = "black"
    )
    
    screen.draw.text(
        "Puntuacion: " + str(score),
        (310 , 20),
        fontname = "pixel",
        fontsize = 18,
        color = "black"
    )

    screen.draw.text(
        "Nivel: " + str(difficulty_level),
        (650, 20),
        fontname = "pixel",
        fontsize = 18,
        color = "black"
    )    

    # GAME OVER
    if game_over:

        screen.fill("black")

        screen.draw.text(
            "GAME OVER",
            center=(WIDTH // 2, HEIGHT // 2 - 30),
            fontname = "pixel",
            fontsize=70,
            color="red"
        )

        screen.draw.text(
            "Puntuacion: " + str(score),
            center = (WIDTH // 2, HEIGHT // 2 + 40),
            fontname = "pixel",
            fontsize = 30,
            color = "white"
        )

        screen.draw.text(
            "Pulsa M para volver al menu",
            center = (WIDTH // 2, 400),
            fontname = "pixel",
            fontsize = 15,
            color = "yellow"
        )

    # VICTORIA
    if game_won:

        screen.fill("darkgreen")

        screen.draw.text(
            "!VICTORIA!",
            center = (WIDTH // 2, 150),
            fontname = "pixel",
            fontsize = 70,
            color = "yellow"
        )

        screen.draw.text(
            "Has consegido 50 monedas",
            center = (WIDTH // 2, 220),
            fontname = "pixel",
            fontsize = 25,
            color = "white"
        )

        screen.draw.text(
            "!Encontraste el cofre!",
            center = (WIDTH // 2, 270),
            fontname = "pixel",
            fontsize = 25,
            color = "white"
        )

        screen.draw.text(
            "Pulsa M para volver al menu",
            center = (WIDTH // 2, 360),
            fontname = "pixel",
            fontsize = 18,
            color = "yellow"
        )

def update():

    global score
    global lives
    global enemy_speed
    global game_started
    global game_over
    global game_won
    global velocity_y
    global on_ground
    global spawn_timer
    global player_frame
    global player_animation_timer
    global player_fancing_left
    global player_idle_frame
    global player_idle_timer
    global coin_frame
    global coin_animation_timer
    global turtle_active
    global turtle_frame
    global turtle_animation_timer

    # PANTALLA DE INICIO
    if not game_started:
        update_sound_button()
        return

    # GAME OVER
    if game_over:
        if keyboard.m:
            return_to_menu()
        return

    # VICTORIA
    if game_won:
        if keyboard.m:
            return_to_menu()
        return

    # MOVIMIENTO DEL JUGADOR
    player_moving = False

    if keyboard.d:
        player.x += 5
        player_moving = True
        player_fancing_left = False

    if keyboard.a:
        player.x -= 5
        player_moving = True
        player_fancing_left = True

    if player_moving:
        player_idle_frame = 0
        player_idle_timer = 0
        player_animation_timer += 1

        if player_animation_timer >= player_animation_speed:
            player_animation_timer = 0
            player_frame += 1

            if player_fancing_left:

                if player_frame >= len(player_frames_l):
                    player_frame = 0

                player.image = player_frames_l[player_frame]

            else:

                if player_frame >= len(player_frames_r):
                    player_frame = 0

                player.image = player_frames_r[player_frame]
    else:
        player_frame = 0
        player_animation_timer = 0
        player_idle_timer += 1

        if player_idle_timer >= player_idle_speed:
            player_idle_timer = 0
            player_idle_frame += 1

            if player_fancing_left:

                if player_idle_frame >= len(player_idle_frames_l):
                    player_idle_frame = 0

                player.image = player_idle_frames_l[player_idle_frame]

            else:

                if player_idle_frame >= len(player_idle_frames_r):
                    player_idle_frame = 0

                player.image = player_idle_frames_r[player_idle_frame]


    # LIMITE DE LA PANTALLA
    if player.left < 0:
        player.left = 0

    if player.right > WIDTH:
        player.right = WIDTH

    # SALTO
    if keyboard.space and on_ground:
        velocity_y = jump_strength
        on_ground = False

    # GRAVEDAD
    velocity_y += gravity
    player.y += velocity_y

    # COLISION CON PLATAFORMAS
    on_ground = False

    for platform in platforms:
        if velocity_y >= 0:
            if (
                player.bottom >= platform.top
                and player.bottom <= platform.top + 15
                and player.right > platform.left
                and player.left < platform.right
            ):
                player.bottom = platform.top
                velocity_y = 0
                on_ground = True

    # SUELO
    if player.bottom > HEIGHT:
        player.bottom = HEIGHT
        velocity_y = 0
        on_ground = True

    # NUEVOS ENEMIGOS 1
    spawn_timer += 1
    if (
        spawn_timer >= spawn_interval
        and len(enemies) < max_enemies
        ):
        create_enemy()
        spawn_timer = 0

    # NUEVO ENEMIGO 2
    if score >= 20 and not turtle_active:
        create_turtle()

    # MOVIMIENTO DEL ENEMIGO 1
    for enemy in enemies:
        enemy.y += enemy_speed
        enemy.animation_timer += 1

        if enemy.animation_timer >= enemy_animation_speed:
            enemy.animation_timer = 0
            enemy.frame += 1

            if enemy.frame >= len(enemy_frames):
                enemy.frame = 0

            enemy.image = enemy_frames[enemy.frame]

    # MOVIMIENTO DEL ENEMIGO 2
    if turtle_active:
        turtle.x -= turtle_speed

    # ELIMINAR ENEMIGOS 1 FUERA DE PANTALLA
    for enemy in enemies[:]:
        if enemy.top > HEIGHT:
            enemies.remove(enemy)

    # ELIMINAR ENEMIGOS 2 FUERA DE PANTALLA
    if turtle_active and turtle.right < 0:
        turtle.x = WIDTH + turtle.width // 2
        turtle.bottom = platforms[0].top

    # ANIMACION DEL ENEMIGO 2
    if turtle_active:
        turtle_animation_timer += 1

        if turtle_animation_timer >= turtle_animation_speed:
            turtle_animation_timer = 0
            turtle_frame += 1

            if turtle_frame >= len(turtle_frames):
                turtle_frame = 0

            turtle.image = turtle_frames[turtle_frame]

    # COMPROBAR SI CHOCO CON EL ENEMIGO 1
    for enemy in enemies[:]:
        if player.colliderect(enemy):
            lives -= 1
            play_sound(sounds.hit)
            enemies.remove(enemy)

            # GAME OVER
            if lives <= 0:
                game_over = True
                music.stop()
                play_sound(sounds.gameover)
                return

    # COMPROBAR SI CHOCO CON EL ENEMIGO 2
    if turtle_active and player.colliderect(turtle):
        lives -= 1
        play_sound(sounds.hit)
        turtle.x = WIDTH + turtle.width // 2
        turtle.bottom = platforms[0].top

        if lives <= 0:
            game_over = True
            music.stop()
            play_sound(sounds.gameover)
            return

    # COMPROBAR SI COGIO LA MONEDA
    if player.colliderect(coin):
        score += 1
        play_sound(sounds.coin)
        coin.pos = (
            random.randint(50, 750),
            random.randint(50, 400)
        )

        update_difficulty()

    # ANIMACION DE LA MONEDA
    coin_animation_timer += 1
    if coin_animation_timer >= coin_animation_speed:
        coin_animation_timer = 0
        coin_frame += 1

        if coin_frame >= len(coin_frames):
            coin_frame = 0

        coin.image = coin_frames[coin_frame]

    # COFRE
    if score >= 50 and player.colliderect(chest):
        game_won = True
        enemies.clear()
        music.stop()
        play_sound(sounds.victory)
        return

# CLICK DEL MOUSE EN BOTONES
def on_mouse_down(pos, button):

    if game_started:
        return

    # BOTON JUGAR
    if play_button.collidepoint(pos):
        play_button.image = "play_button_pressed"

    # BOTON SONIDO
    elif sound_button.collidepoint(pos):
        if sound_enable:
            sound_button.image = "sound_on_pressed"
        else:
            sound_button.image = "sound_off_pressed"

    # BOTON SALIR
    elif exit_button.collidepoint(pos):
        exit_button.image = "exit_button_pressed"

# SOLTAR CLICK DEL MOUSE
def on_mouse_up(pos, button):

    global game_started
    global sound_enable

    if game_started:
        return

    # JUGAR
    if play_button.collidepoint(pos):
        play_button.image = "play_button"
        reset_game()
        game_started = True

    # SONIDO
    elif sound_button.collidepoint(pos):
        sound_enable = not sound_enable
        update_sound_button()
        update_music()

    # SALIR
    elif exit_button.collidepoint(pos):
        quit()

    # RESTAURAR BOTONES
    play_button.image = "play_button"
    exit_button.image = "exit_button"
    update_sound_button()

update_music()

pgzrun.go()