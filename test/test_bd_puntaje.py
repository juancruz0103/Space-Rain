import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
import sqlite3
from bd_puntaje import Puntaje

class TestPuntaje(unittest.TestCase):
    
    def setUp(self):
        # Crear una instancia de la clase Puntaje y una base de datos en memoria para pruebas
        self.puntaje = Puntaje()
        self.puntaje.conexion = sqlite3.connect(":memory:")
        self.puntaje.cursor = self.puntaje.conexion.cursor()
        self.puntaje.cursor.execute('''
            CREATE TABLE IF NOT EXISTS puntuaciones (
                nombre TEXT UNIQUE,
                puntuacion INTEGER
            )
        ''')
        self.puntaje.conexion.commit()
    
    def tearDown(self):
        # Cerrar la conexión a la base de datos
        self.puntaje.cerrar()
    
    def test_insertar(self):
        # Probar la inserción de datos
        self.assertTrue(self.puntaje.insertar("Jugador1", 300))
        self.puntaje.cursor.execute("SELECT * FROM puntuaciones WHERE nombre = 'Jugador1'")
        resultado = self.puntaje.cursor.fetchone()
        self.assertIsNotNone(resultado)
        self.assertEqual(resultado[0], "Jugador1")
        self.assertEqual(resultado[1], 300)
    
    def test_insertar_nombre_duplicado(self):
        # Probar la inserción de un nombre duplicado
        self.assertTrue(self.puntaje.insertar("Jugador1", 100))
        self.assertFalse(self.puntaje.insertar("Jugador1", 200))
    
    def test_mostrar(self):
        # Probar la función mostrar
        self.puntaje.insertar("Jugador1", 300)
        self.puntaje.insertar("Jugador2", 200)
        resultados = self.puntaje.mostrar()
        self.assertEqual(len(resultados), 2)
        self.assertEqual(resultados[0][0], "Jugador1")
        self.assertEqual(resultados[0][1], 300)
        self.assertEqual(resultados[1][0], "Jugador2")
        self.assertEqual(resultados[1][1], 200)

if __name__ == "__main__":
    unittest.main()