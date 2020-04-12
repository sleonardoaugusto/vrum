import unittest
from core.direcao import Direcao, Direcoes
from core.motor import Motor


class Carro:
    def __init__(self):
        self.velocidade = Motor().velocidade
        self.direcao = Direcao().direcao


class CarroTest(unittest.TestCase):
    def setUp(self) -> None:
        self.c = Carro()

    def test_velocidade(self):
        self.assertEqual(self.c.velocidade, 0)

    def test_direcao(self):
        self.assertEqual(self.c.direcao, Direcoes.Norte.name)
