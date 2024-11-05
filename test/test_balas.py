import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from balas import Balas

class TestBalas(unittest.TestCase):
    
    def setUp(self):
        # Inicializar Pygame y crear una ventana para las pruebas
        pygame.init()
        self.ventana = pygame.display.set_mode((1000, 600))
        # Crear una instancia de la clase Balas para las pruebas
        self.bala = Balas(500, 500)
    
    def tearDown(self):
        # Cerrar Pygame después de cada prueba
        pygame.quit()
    
    def test_bala_inicializacion(self):
        # Probar la inicialización de la bala
        self.assertEqual(self.bala.x, 500)
        self.assertEqual(self.bala.y, 500)
        self.assertEqual(self.bala.ancho, 20)
        self.assertEqual(self.bala.alto, 20)
        self.assertEqual(self.bala.velocidad, 8)
    
    def test_bala_dibujar(self):
        # Probar el método dibujar de la bala
        self.bala.dibujar(self.ventana)
        self.assertIsInstance(self.bala.rect, pygame.Rect)
    
    def test_bala_movimiento(self):
        # Probar el método movimiento de la bala
        y_inicial = self.bala.y
        self.bala.movimiento()
        self.assertEqual(self.bala.y, y_inicial - self.bala.velocidad)

if __name__ == "__main__":
    unittest.main()