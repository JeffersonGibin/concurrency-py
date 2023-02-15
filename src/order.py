
from datetime import datetime
import math
import random

class Order:
    def __init__(self, dados: dict) -> None:
        self.numero_pedido = math.ceil(random.randint(1, 999999))
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        self.nome =  dados.get("client_name"),
        self.pedido = dados.get("order"),

    def get(self):
        nome, = self.nome
        return {
            "numero_pedido": self.numero_pedido,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "pedido": self.pedido,
            "cliente": nome,
        }

