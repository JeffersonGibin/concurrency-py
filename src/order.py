
from datetime import datetime
import math
import random

class Order:
    def __init__(self, dados: dict) -> None:
        self.numero_pedido = math.ceil(random.randint(1, 999999))
        self.data = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        self.nome =  dados.get("client_name"),
        self.pedido = dados.get("order_itens"),

    def get(self):
        nome, = self.nome
        return {
            "order_number": self.numero_pedido,
            "date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            "order_itens": self.pedido,
            "client_name": nome,
        }

