import unittest
import enum


class Direcoes(enum.Enum):
    Norte = 1
    Leste = 2
    Sul = 3
    Oeste = 4


class Direcao:

    def __init__(self):
        self._direcao = Direcoes.Norte.name

    def girar(self, direcao):
        value = Direcoes[self._direcao].value
        if direcao == 'direita':
            value = 1 if value == 4 else value + 1
        if direcao == 'esquerda':
            value = 4 if value == 1 else value - 1
        self._direcao = Direcoes(value).name


class TestDirecao(unittest.TestCase):
    def setUp(self) -> None:
        self.d = Direcao()

    def test_girar(self):
        self.assertEqual(self.d._direcao, Direcoes.Norte.name)
        self.d.girar(direcao='direita')
        self.assertEqual(self.d._direcao, Direcoes.Leste.name)
        self.d.girar(direcao='direita')
        self.assertEqual(self.d._direcao, Direcoes.Sul.name)
        self.d.girar(direcao='direita')
        self.assertEqual(self.d._direcao, Direcoes.Oeste.name)
        self.d.girar(direcao='direita')
        self.assertEqual(self.d._direcao, Direcoes.Norte.name)
        self.d.girar(direcao='esquerda')
        self.assertEqual(self.d._direcao, Direcoes.Oeste.name)
        self.d.girar(direcao='esquerda')
        self.assertEqual(self.d._direcao, Direcoes.Sul.name)
        self.d.girar(direcao='esquerda')
        self.assertEqual(self.d._direcao, Direcoes.Leste.name)
        self.d.girar(direcao='esquerda')
        self.assertEqual(self.d._direcao, Direcoes.Norte.name)
