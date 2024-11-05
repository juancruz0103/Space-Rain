import pygame

#creamos la clase Balas
class Balas:
    
    #creamos el constructor de la clase Balas con los atributos x y y que vienen a ser las coordenadas de las balas en la ventana
    def __init__(self , x, y):
        self.x = x
        self.y = y
        self.ancho = 20
        self.alto = 20
        self.velocidad = 8
        self.color = "white"
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) 
        self.imagen = pygame.image.load("recursos/balas.png")
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho, self.alto))
        self.imagen = pygame.transform.rotate(self.imagen , 90)
        
        
    def dibujar(self , ventana):
        #creamos un rectangulo con las coordenadas de las balas y el color que luego sera reemplazado por la imagen de las balas
        self .rect = pygame.Rect(self.x, self.y, self.ancho, self.alto) 
        # pygame.draw.rect(ventana, self.color, self.rect)
        
        #imprimimos la imagen de las balas en la ventana
        ventana.blit(self.imagen, (self.x, self.y))
        
        #creamos la funcion para el movimiento de las balas
    def movimiento(self):
        self.y -= self.velocidad