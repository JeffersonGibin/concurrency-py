from ast import List
from src.adapters.producer_rabbit import ProducerRabbitMQ
from src.table import Table
from src.order import Order

class Waiter:
    def __init__(self, id: int, producer: ProducerRabbitMQ) -> None:
        self.orders = []
        self.id = id
        self.producer = producer
    
    def write_orders(self, order: Order, table: Table):
        order = order.get()
        custumer_name = order.get("client_name")
        date = order.get("date")
        order_itens = order.get("order_itens")
        order_number = order.get("order_number")
       
        self.orders.append({
            "table_number": table.random_table_number,
            "client_name": custumer_name,
            "order_number": order_number,
            "date": date,
            "order_itens": order_itens
        })

    def send_order_to_kitchen(self):
        for order in self.orders:
            self.producer.publish(order)


