import unittest
from PruebaXalDigital import *

class TestProccess(unittest.TestCase):

    def test_anwers(self):
        # se genera una variable con la informacion de la data
        data_set = data_items
        # se genera una variable contador
        cont = 0
        # se realiza la prueba
        result = Proccess.anwers(data_set,cont,'is_answered')
        self.assertEqual(result, 'Repuestas\nContestadas : 22\nNo contestadas : 8')

    def test_minor_views(self):
        # se genera una variable con la informacion de la data
        data_set = data_items
        # se genera una variable contador
        cont = 0
        # se realiza la prueba
        result = Proccess.minor_views(data_set,cont,'view_count')
        self.assertEqual(result, 'Menor Vista\nRespuesta n.: 10\nNumero de vistas : 10')

    def test_anwers_hold_new(self):
        # se genera una variable con la informacion de la data
        data_set = data_items
        # se genera una variable contador
        cont = 0
        # se realiza la prueba
        result = Proccess.anwers_hold_new(data_set,cont,'creation_date')
        self.assertEqual(result, 'Respuesta\nMas vieja : 4  = 1674226749\nMas Nueva : 11  = 1231709322')
    
    def test_elderly_reputation(self):
        # se genera una variable con la informacion de la data
        data_set = data_items
        # se genera una variable contador
        cont = 0
        # se realiza la prueba
        result = Proccess.elderly_reputation(data_items,cont,'owner','reputation')
        self.assertEqual(result, 'Mayor Reputacion\nRespuesta n.: 11\nReputacion : 925042')

if __name__ == '__main__':
    unittest.main()