import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import pygame
from main import crear_balas, gestion_teclas, nave, balas

class TestMain(unittest.TestCase):
    
    def setUp(self):
        # Inicializar Pygame y crear una ventana para las pruebas
        pygame.init()
        self.ventana = pygame.display.set_mode((1000, 600))
    
    def tearDown(self):
        # Cerrar Pygame después de cada prueba
        pygame.quit()
    
    def test_crear_balas(self):
        # Probar la creación de balas
        balas_iniciales = len(balas)
        crear_balas()
        self.assertEqual(len(balas), balas_iniciales + 1)
    
    def test_gestion_teclas(self):
        # Probar la gestión de teclas
        teclas = pygame.key.get_pressed()
        nave.x = 500
        nave.y = 500
        gestion_teclas(teclas)
        self.assertEqual(nave.x, 500)
        self.assertEqual(nave.y, 500)

if __name__ == "__main__":
    unittest.main()