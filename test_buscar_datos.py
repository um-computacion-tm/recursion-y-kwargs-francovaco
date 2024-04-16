import unittest
from main import database 
from main import buscar_datos

class TestDatabase(unittest.TestCase):
    def test_buscar_datos(self): 
        persona = {"primer_nombre": "Pablo", "segundo_nombre": "Diego", "primer_apellido": "Ruiz", "segundo_apellido": "Picasso"}
        self.assertEqual(buscar_datos(persona, database), True)
    def test_buscar_datos1(self): 
        persona = {"primer_nombre": "Diego", "segundo_nombre": "Alejandro", "primer_apellido": "Barroso", "segundo_apellido": "Miller"}
        self.assertEqual(buscar_datos(persona, database), False)
    def test_buscar_datos2(self):
        persona = {"primer_nombre": "Maria", "segundo_nombre": "Luisa", "primer_apellido": "Galera", "segundo_apellido": "Suarez"}
        self.assertEqual(buscar_datos(persona, database), False)
    def test_buscar_datos3(self):
        persona = {"primer_nombre": "Manuel", "segundo_nombre": "Jose", "primer_apellido": "Diez", "segundo_apellido": "Ramirez"}
        self.assertEqual(buscar_datos(persona, database), False)
    def test_buscar_datos4(self):
        persona = {"primer_nombre": "Pablo", "segundo_nombre": "", "primer_apellido": "Ruiz", "segundo_apellido": "Picasso"}
        self.assertEqual(buscar_datos(persona, database), False)
    def test_buscar_datos5(self):
        persona = {"segundo_nombre": "Diego", "primer_nombre": "Pablo", "segundo_apellido": "Picasso", "primer_apellido": "Ruiz"}
        self.assertEqual(buscar_datos(persona, database), True)
    def test_buscar_datos6(self):
        persona = {"segundo_nombre": "Jose", "segundo_apellido": "Oñate", "primer_nombre": "Manuel", "primer_apellido": "Diez"}
        self.assertEqual(buscar_datos(persona, database), True)
    def test_buscar_datos7(self):
        persona = {"segundo_apellido": "Chuajer", "primer_apellido": "Yañes", "segundo_nombre": "Tomas", "primer_nombre": "Franco"}
        self.assertEqual(buscar_datos(persona, database), True)

unittest.main()