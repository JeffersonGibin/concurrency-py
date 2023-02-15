from src.order import Order


class Custumer:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_order(self, order_dict: dict) -> Order:
        name = self.name
        order =  Order({
            "custumer_name": name,
            "order": order_dict,
        })

        return order