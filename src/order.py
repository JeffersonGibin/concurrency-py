
from datetime import datetime
import math
import random

class Order:
    def __init__(self, data: dict) -> None:
        self.random_order_number = math.ceil(random.randint(1, 999999))
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        self.client_name =  data.get("client_name"),
        self.order_itens = data.get("order_itens"),

    def get(self):
        client_name, = self.client_name
        return {
            "order_number": self.random_order_number,
            "date": self.date,
            "order_itens": self.order_itens,
            "client_name": client_name,
        }

