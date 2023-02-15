from src.order import Order


class Client:
    def __init__(self, name) -> None:
        self.name = name
    
    def make_order(self, order_dict: dict) -> Order:
        client: dict = self.name
        order =  Order({
            "client_name": client,
            "order": order_dict,
        })

        return order