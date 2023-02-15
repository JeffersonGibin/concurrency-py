
from datetime import datetime
import math
import random

class Order:
    def __init__(self, data: dict) -> None:
        self.random_order_number = math.ceil(random.randint(1, 999999))
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        self.custumer_name =  data.get("custumer_name"),
        self.order_items = data.get("order_items"),

    def get(self):
        custumer_name, = self.custumer_name
        return {
            "order_number": self.random_order_number,
            "date": self.date,
            "order_items": self.order_items,
            "custumer_name": custumer_name,
        }

