import unittest


class Direcao:
    NORTE = 'N'
    LESTE = 'L'
    SUL = 'S'
    OESTE = 'O'

    def __init__(self):
        self.direcao = self.NORTE

    def girar_a_direita(self):
        if self.direcao == self.NORTE:
            self.direcao = self.LESTE
        elif self.direcao == self.LESTE:
            self.direcao = self.SUL
        elif self.direcao == self.SUL:
            self.direcao = self.OESTE
        else:
            self.direcao = self.NORTE

    def girar_a_esquerda(self):
        if self.direcao == self.OESTE:
            self.direcao = self.SUL
        elif self.direcao == self.SUL:
            self.direcao = self.LESTE
        elif self.direcao == self.LESTE:
            self.direcao = self.NORTE
        else:
            self.direcao = self.OESTE


class TestDirecao(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Direcao()

    def test_girar_a_direita(self):
        self.assertEqual(self.d.direcao, self.d.NORTE)
        self.d.girar_a_direita()
        self.assertEqual(self.d.direcao, self.d.LESTE)
        self.d.girar_a_direita()
        self.assertEqual(self.d.direcao, self.d.SUL)
        self.d.girar_a_direita()
        self.assertEqual(self.d.direcao, self.d.OESTE)
        self.d.girar_a_direita()
        self.assertEqual(self.d.direcao, self.d.NORTE)

    def test_girar_a_esquerda(self):
        self.assertEqual(self.d.direcao, self.d.NORTE)
        self.d.girar_a_esquerda()
        self.assertEqual(self.d.direcao, self.d.OESTE)
        self.d.girar_a_esquerda()
        self.assertEqual(self.d.direcao, self.d.SUL)
        self.d.girar_a_esquerda()
        self.assertEqual(self.d.direcao, self.d.LESTE)
        self.d.girar_a_esquerda()
        self.assertEqual(self.d.direcao, self.d.NORTE)
