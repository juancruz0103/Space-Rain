import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from personaje import Nave

class TestNave(unittest.TestCase):
    
    def setUp(self):
        # Inicializar Pygame y crear una ventana para las pruebas
        pygame.init()
        self.ventana = pygame.display.set_mode((1000, 600))
        # Crear una instancia de la clase Nave para las pruebas
        self.nave = Nave(500, 500)
    
    def tearDown(self):
        # Cerrar Pygame después de cada prueba
        pygame.quit()
    
    def test_nave_inicializacion(self):
        # Probar la inicialización de la nave
        self.assertEqual(self.nave.x, 500)
        self.assertEqual(self.nave.y, 500)
        self.assertEqual(self.nave.ancho, 50)
        self.assertEqual(self.nave.alto, 50)
        self.assertEqual(self.nave.velocidad, 10)
    
    def test_nave_dibujar(self):
        # Probar el método dibujar de la nave
        self.nave.dibujar(self.ventana)
        self.assertIsInstance(self.nave.rect, pygame.Rect)

if __name__ == "__main__":
    unittest.main()