import pygame

#creamos la clase Enemigo
class Enemigo:
    
    #creamos el constructor de la clase Enemigo con los atributos x y y que vienen a ser las coordenadas de los enemigos en la ventana
    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.ancho = 50
        self.alto = 50
        self.velocidad = 3
        self.color = "purple"
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) #creamos un rectangulo con las coordenadas de los enemigos
        self.vida = 1 
        self.imagen = pygame.image.load("recursos/rocas.png") #cargamos la imagen de los enemigos
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto)) #escalamos la imagen de los enemigos
        
        
    def dibujar(self , ventana):
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) 
        #dibujamos un rectangulo con las coordenadas de los enemigos y el color que luego sera reemplazado por la imagen de los enemigos
        # pygame.draw.rect(ventana, self.color, self.rect)
        
        #imprimimos la imagen de los enemigos en la ventana
        ventana.blit(self.imagen, (self.x , self.y))
        
    #creamos la funcion para el movimiento de los enemigos    
    def movimiento(self):
        self.y += self.velocidad