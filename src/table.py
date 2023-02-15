import math
import random

from src.client import Client

class Table:
    def __init__(self) -> None:
        self.clientes = []
        self.mesa_id = math.ceil(random.randint(1, 15))

    def receber_cliente(self, cliente: Client) -> None:
        self.clientes.append(cliente)

    def clientes_mesa(self) -> list:
        return self.clientes
