#importamos sqlite3
import sqlite3

#creamos la base de datos
class Puntaje:
    
    #creamos el constructor de la clase Base_de_datos
    def __init__(self):
        self.conexion = sqlite3.connect("puntaje.db") #creamos la conexion con la base de datos
        self.cursor = self.conexion.cursor() #creamos el cursor para ejecutar las consultas
        
        #creamos la tabla puntuaciones
        self.cursor.execute("CREATE TABLE IF NOT EXISTS puntuaciones (nombre TEXT UNIQUE, puntuacion INTEGER)")
        self.conexion.commit()
        
    #creamos la funcion para insertar los datos en la tabla puntuaciones
    def insertar(self, nombre, puntuacion):
        self.cursor.execute("SELECT * FROM puntuaciones WHERE nombre = ?", (nombre,))
        if self.cursor.fetchone() is None:
            self.cursor.execute("INSERT INTO puntuaciones VALUES (?, ?)", (nombre, puntuacion))
            self.conexion.commit()
            return True
        else:
            return False
        
    #creamos la funcion para mostrar los datos de la tabla puntuaciones
    def mostrar(self):
        self.cursor.execute("SELECT * FROM puntuaciones ORDER BY puntuacion DESC")
        return self.cursor.fetchall()
    
    #creamos la funcion para cerrar la conexion con la base de datos
    def cerrar(self):
        self.conexion.close()