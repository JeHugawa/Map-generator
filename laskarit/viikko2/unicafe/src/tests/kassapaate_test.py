import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        testcafe = Kassapaate() 

    def test_rahamaara_ja_myytyjen_maara_oikea(self):
        self.assertEqual(testcafe.kassassa_rahaa, 100000)
        self.assertEqual(testcafe.edulliset, 0)
        self.assertEqual(testcafe.maukkaat, 0)

    def test_syo_maukkaasti_kateisella_kun_riittava(self):
        a = testcafe.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(testcafe.kassassa_rahaa, 100400)
        self.assertEqual(testcafe.maukkaat, 1)
        self.assertEqual(a, 100)

