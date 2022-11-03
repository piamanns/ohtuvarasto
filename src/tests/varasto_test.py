import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_luonti_negatiivisella_tilavuudella_nollaa_tilavuuden(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_uudella_varastolla_oikea_saldo(self):
        varasto = Varasto(20, 10)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_uuden_varaston_luonti_negatiivisella_saldolla_nollaa_saldon(self):
        varasto = Varasto(100, -20)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_uudella_varastolla_oikea_saldo_jos_annettu_saldo_suurempi_kuin_tilavuus(self):    
        tilavuus = 20
        saldo = 200
        varasto = Varasto(tilavuus, saldo)
        self.assertAlmostEqual(varasto.saldo, tilavuus)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivisen_maaran_lisays_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_lisays_ei_muuta_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_suuremman_maaran_lisaaminen_kuin_mahtuu_asettaa_saldon_yhta_suureksi_kuin_tilavuus(self):
        self.varasto.lisaa_varastoon(18)
        self.assertAlmostEqual(self.varasto.saldo, 10)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_vahentaa_saldoa_oikein(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(5)

        self.assertAlmostEqual(self.varasto.saldo, 3)
    
    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        self.varasto.lisaa_varastoon(7)

        saatu_maara = self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(saatu_maara, 0)
    
    def test_negatiivisen_maaran_ottaminen_ei_muuta_tilaa(self):
        self.varasto.lisaa_varastoon(7)
        # varastoon jää tilaa 10 - 7 = 3

        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 3)
    
    def test_isomman_maaran_ottaminen_kuin_saldo_palauttaa_koko_saldon(self):
      self.varasto.lisaa_varastoon(8)

      saatu_maara = self.varasto.ota_varastosta(15)

      self.assertAlmostEqual(saatu_maara, 8)

    def test_isomman_maaran_ottaminen_kuin_saldo_nollaa_saldon(self):
      self.varasto.lisaa_varastoon(8)

      self.varasto.ota_varastosta(15)

      self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_isomman_maaran_ottaminen_kuin_saldo_vapauttaa_koko_tilavuuden_kayttoon(self):
      self.varasto.lisaa_varastoon(8)

      self.varasto.ota_varastosta(15)

      self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_str_palauttaa_oikein_muodostetun_merkkijonon(self):
        self.varasto.lisaa_varastoon(8)
        # saldo nyt 8, varastossa vielä tilaa 2

        merkkijono = str(self.varasto)

        self.assertEqual(merkkijono, "saldo = 8, vielä tilaa 2")
