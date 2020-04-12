import unittest


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade < 2:
            self.velocidade = 0
        else:
            self.velocidade -= 2


class MotorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.m = Motor()

    def test_acelerar(self):
        """Acelerar deve incrementar velocidade ao passo de 1"""
        self.m.acelerar()
        self.assertEqual(self.m.velocidade, 1)
        self.m.acelerar()
        self.assertEqual(self.m.velocidade, 2)
        self.m.acelerar()
        self.assertEqual(self.m.velocidade, 3)
        self.m.acelerar()
        self.assertEqual(self.m.velocidade, 4)

    def test_frear(self):
        """
        Frear deve decrementar velocidade ao passo de 2
        Velocidade deve ter valor mínimo de 0
        """
        self.m.velocidade = 0
        self.m.frear()
        self.assertEqual(self.m.velocidade, 0)
        self.m.velocidade = 1
        self.m.frear()
        self.assertEqual(self.m.velocidade, 0)
        self.m.velocidade = 2
        self.m.frear()
        self.assertEqual(self.m.velocidade, 0)
        self.m.velocidade = 3
        self.m.frear()
        self.assertEqual(self.m.velocidade, 1)
        self.m.velocidade = 4
        self.m.frear()
        self.assertEqual(self.m.velocidade, 2)
