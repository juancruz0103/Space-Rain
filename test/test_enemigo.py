import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from enemigo import Enemigo

class TestEnemigo(unittest.TestCase):
    
    def setUp(self):
        # Inicializar Pygame y crear una ventana para las pruebas
        pygame.init()
        self.ventana = pygame.display.set_mode((1000, 600))
        # Crear una instancia de la clase Enemigo para las pruebas
        self.enemigo = Enemigo(500, 100)
    
    def tearDown(self):
        # Cerrar Pygame después de cada prueba
        pygame.quit()
    
    def test_enemigo_inicializacion(self):
        # Probar la inicialización del enemigo
        self.assertEqual(self.enemigo.x, 500)
        self.assertEqual(self.enemigo.y, 100)
        self.assertEqual(self.enemigo.ancho, 50)
        self.assertEqual(self.enemigo.alto, 50)
        self.assertEqual(self.enemigo.velocidad, 3)
        self.assertEqual(self.enemigo.vida, 1)
    
    def test_enemigo_dibujar(self):
        # Probar el método dibujar del enemigo
        self.enemigo.dibujar(self.ventana)
        self.assertIsInstance(self.enemigo.rect, pygame.Rect)
    
    def test_enemigo_movimiento(self):
        # Probar el método movimiento del enemigo
        y_inicial = self.enemigo.y
        self.enemigo.movimiento()
        self.assertEqual(self.enemigo.y, y_inicial + self.enemigo.velocidad)

if __name__ == "__main__":
    unittest.main()