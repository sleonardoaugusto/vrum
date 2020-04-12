import unittest
from core.direcao import Direcao, Direcoes
from core.motor import Motor


class Carro:
    def __init__(self, motor, direcao):
        self.motor = motor
        self.direcao = direcao

    def calcular_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcular_direcao(self):
        return self.direcao.valor


class CarroTest(unittest.TestCase):
    def setUp(self) -> None:
        motor = Motor()
        direcao = Direcao()
        self.c = Carro(motor, direcao)

    def test_instance(self):
        self.assertIsInstance(self.c.motor, Motor)
        self.assertIsInstance(self.c.direcao, Direcao)
