import pygame
#creamos la clase Nave
class Nave:
    #creamos el constructor de la clase Nave con los atributos x y y que vienen a ser las coordenadas de la nave en la ventana
    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 10 #creamos la velocidad de la nave para que se mueva
        self.color = "red"
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #creamos un rectangulo con las coordenadas de la nave
        self.imagen = pygame.image.load("recursos/nave.png") #cargamos la imagen de la nave
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto)) #escalamos la imagen de la nave
        
        
    def dibujar(self , ventana):
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #creamos un rectangulo con las coordenadas de la nave
        
        #dibujamos un rectangulo con las coordenadas de la nave y el color que luego sera reemplazado por la imagen de la nave
        # pygame.draw.rect(ventana, self.color, self.rect) 
        
        #imprimimos la imagen de la nave en la ventana
        ventana.blit(self.imagen, (self.x , self.y))