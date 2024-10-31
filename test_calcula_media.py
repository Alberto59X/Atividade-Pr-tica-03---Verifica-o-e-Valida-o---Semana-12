import unittest
from media_calculator import calcula_media

class TestCalculaMedia(unittest.TestCase):

    def test_media_notas_inteiras(self):
        "Testa a média com notas inteiras."
        resultado = calcula_media(10, 5, 7)
        self.assertEqual(resultado, 7.33, f"Esperado 7.33, mas obteve {resultado}")

    def test_media_notas_zero(self):
        "Testa a média quando todas as notas são zero."
        resultado = calcula_media(0, 0, 0)
        self.assertEqual(resultado, 0, f"Esperado 0, mas obteve {resultado}")

    def test_media_notas_maximas(self):
        "Testa a média quando todas as notas estão no valor máximo."
        resultado = calcula_media(10, 10, 10)
        self.assertEqual(resultado, 10, f"Esperado 10, mas obteve {resultado}")

    def test_media_notas_decimais(self):
        "Testa a média com valores decimais."
        resultado = calcula_media(7.5, 8.3, 9.2)
        self.assertAlmostEqual(resultado, 8.33, places=2, msg=f"Esperado aproximadamente 8.33, mas obteve {resultado}")

if __name__ == '__main__':
    unittest.main()

