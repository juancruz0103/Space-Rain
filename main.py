#importamos la libreria pygame
import pygame


#importamos random
import random

#importamos las clases que creamos
from personaje import Nave
from enemigo import Enemigo
from balas import Balas
from bd_puntaje import Puntaje

#inicializamos la base de datos
puntuaciones = Puntaje()

#inicializamos pygame
pygame.init()

#inicializamos el modulo de sonido
pygame.mixer.init()

#creamos la ventana con su respectivo titulo
pygame.display.set_caption("Space Rain") 

#definimos las variables
ANCHO= 1000
ALTO = 600
FPS = 60
FUENTE = pygame.font.SysFont("MV Boli", 40)

#creamos la musica de fondo
pygame.mixer.music.load('recursos/sonido_juego.mp3')
pygame.mixer.music.play(-1) #reproduce la musica de fondo en bucle

#Establecemos los sonidos
SONIDO_BALA = pygame.mixer.Sound('recursos/disparos.mp3')
SONIDO_MUERTE_ENEMIGO = pygame.mixer.Sound('recursos/muerte_rocas.wav')



#creamos la ventana
VENTANA = pygame.display.set_mode((ANCHO, ALTO)) 

#creamos un bucle para mantener la ventana abierta
jugando = True

#creamos el fondo de la ventana con una imagen
fondo = pygame.image.load("recursos/fondo.png")
fondo = pygame.transform.scale(fondo, (ANCHO, ALTO))

#creamos un reloj para controlar los fps
reloj = pygame.time.Clock() 

#creamos la vida y los puntos
vidas = 5
puntos = 0

#creamos las variables para la aparicion de enemigos 
tiempo_de_creacion = 0 #tiempo que ha pasado desde la ultima creacion de enemigos
tiempo_entre_enemigos = 500 #tiempo que tarda en aparecer un nuevo enemigo
tiempo_entre_enemigos_inicial = 1000 #tiempo que tarda en aparecer un nuevo enemigo

#creamos la Nave 
nave = Nave(ANCHO/2, ALTO - 55)

#creamos las liustas de enemigos y balas
enemigos = []
balas = []

#creamos las variables para las balas
ultima_bala = 0 #tiempo que ha pasado desde la ultima bala
tiempo_entre_balas = 200 #tiempo que tarda en aparecer una nueva bala o en otras palabras la cadencia de disparo

#creamos los enemigos iniciales y los agregamos a la lista de enemigos estableciendo su posicion
enemigos.append(Enemigo(ANCHO/2, 100))

#creamos la funcion para crear balas
def crear_balas():
    #declaramos las variables globales
    global ultima_bala
    
    #creamos una condicion para que la bala se cree cada cierto tiempo con la funcion get_ticks() de pygame
    if pygame.time.get_ticks() - ultima_bala > tiempo_entre_balas:
        balas.append(Balas(nave.rect.centerx, nave.rect.centery))
        ultima_bala = pygame.time.get_ticks()
        
    #reproducimos el sonido de la bala cada vez que se dispara
        SONIDO_BALA.play()

#creamos la funcion para gestionar las teclas de movimiento de la nave  y le ponemos un limite para que no se salga de la ventana
def gestion_teclas(teclas):
    if teclas[pygame.K_RIGHT]:
        if nave.x + nave.ancho <= ANCHO:
            nave.x += nave.velocidad
    if teclas[pygame.K_LEFT]:
        if nave.x >= 0:
            nave.x -= nave.velocidad
    if teclas[pygame.K_a]:
        if nave.x >= 0:
            nave.x -= nave.velocidad
    if teclas[pygame.K_d]:
        if nave.x + nave.ancho <= ANCHO:
            nave.x += nave.velocidad
    if teclas[pygame.K_SPACE]:
        crear_balas()
        
    # if teclas[pygame.K_w]:
    #     Nave.y -= Nave.velocidad    
    # if teclas[pygame.K_s]:
    #     Nave.y += Nave.velocidad    


#creamos un bucle para mantener la ventana abierta
while jugando and vidas > 0:
    
    #establecemos los fps
    tiempo_de_creacion += reloj.tick(FPS)
 
    #creamos un bucle para que los enemigos aparezcan cada cierto tiempo  y lo randomizamos con random.randint()
    if tiempo_de_creacion > tiempo_entre_enemigos:
        enemigos.append(Enemigo(random.randint(0, ANCHO), -100))
        tiempo_de_creacion = 0 #reiniciamos el tiempo de creacion
        tiempo_entre_enemigos = random.randint(50 , max(50 ,tiempo_entre_enemigos_inicial)) #randomizamos el tiempo de creacion de los enemigos
    #reducimos el tiempo de creacion de los enemigos cada vez que se crean mas enemigos
        if tiempo_entre_enemigos_inicial > 20:
            tiempo_entre_enemigos_inicial -= 4
    
    #creamos un bucle para mantener la ventana abierta con la funcion get() de pygame
    eventos = pygame.event.get()
    
    #creamos una variable para las teclas
    teclas = pygame.key.get_pressed()
    
    #creamos un texto para las vidas y los puntos
    texto_vidas = FUENTE.render(f"Vidas: {vidas}", True, "white")  
    texto_puntaje = FUENTE.render(f"Puntos: {puntos}", True, "white")  
    
    #llamamos a la funcion de gestion de teclas
    gestion_teclas(teclas)
    
    #creamos un bucle para cerrar la ventana
    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False
    
    #establecemos el color de la ventana con el fondo establecido previamente y lo dibujamos en la ventana
    VENTANA.blit(fondo, (0, 0))
    nave.dibujar(VENTANA)
    
    #creamos un bucle para que los enemigos aparezcan en la ventana y se muevan
    # y a la vez se crea un duplicado de la lista de enemigos para que no ocurra ningun error en el bucle principal
    for enemigo in enemigos[:]:
        enemigo.dibujar(VENTANA)
        enemigo.movimiento()
        
      #creamos un bucle para que los enemigos colisionen con la Nave y se eliminen de la lista de enemigos
        if pygame.Rect.colliderect(nave.rect, enemigo.rect):
            vidas -= 1
            if enemigo in enemigos:
                enemigos.remove(enemigo)
            
      #creamos un bucle para que los enemigos desaparezcan de la ventana y se eliminen de la lista de enemigos      
        if enemigo.y > ALTO:
            if enemigo in enemigos:
                enemigos.remove(enemigo)
            
      #creamos un bucle para que las balas colisionen con los enemigos y se eliminen de la lista de balas
      #ademas de hacer un duplicado de la lista de balas para que no ocurra ningun error en el bucle principal
        for bala in balas[:]:
            if pygame.Rect.colliderect(bala.rect, enemigo.rect):
                enemigo.vida -= 1
                if bala in balas:
                    balas.remove(bala)
                
                
        #creamos la condicion de que cada vez que un enemigo muera se reproduzca el sonido de la muerte del enemigo 
        # y se sumen puntos y se elimine de la lista de enemigos
        if enemigo.vida <= 0:
            SONIDO_MUERTE_ENEMIGO.play()
            if enemigo in enemigos:
                enemigos.remove(enemigo)
            puntos += 10
    
    #creamos un bucle para dibujar las balas en la ventana y que se muevan
    # y a la vez se crea un duplicado de la lista de balas para que no ocurra ningun error en el bucle principal
    for bala in balas[:]:
        bala.dibujar(VENTANA)
        bala.movimiento()
        
        #creamos un bucle para que cuando las balas salgan de la ventana se eliminen de la lista de balas
        if bala.y < 0:
            if bala in balas:
                balas.remove(bala)
    
    #imprimimos los textos de las vidas y los puntos y establecemos su posicion
    VENTANA.blit(texto_vidas, (10, 10))
    VENTANA.blit(texto_puntaje, (10, 70))
    
    #actualizamos la ventana
    pygame.display.flip()
      
#creamos un bucle para que cuando las vidas sean 0 o jugando sea falso se cierre la ventana      
pygame.quit()


#creamos el input para que el jugador pueda ingresar su nombre
nombre = input("\nIngrese su nombre: ")
while not puntuaciones.insertar(nombre, puntos):
    print("El nombre ya existe. Por favor, ingrese un nombre diferente.")
    nombre = input("\nIngrese su nombre: ")

#creamos un bucle para mostrar las puntuaciones
print ("\nPuntuaciones")
for puntuacion in puntuaciones.mostrar():
    print (f"\nNombre: {puntuacion[0]} - Puntos: {puntuacion[1]}")



#creamos un bucle para cerrar la ventana
print("\nGracias por jugar")
    
quit()