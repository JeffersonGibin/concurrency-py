from ast import List
from src.adapters.producer_rabbit import ProducerRabbitMQ
from src.table import Table
from src.order import Order

class Waiter:
    def __init__(self, id: int, producer: ProducerRabbitMQ) -> None:
        self.pedidos = []
        self.id = id
        self.producer = producer
    
    def anota_pedidos(self, pedido: Order, mesa: Table):
        pedido = pedido.get()
        client_name = pedido.get("client_name")
        date = pedido.get("date")
        order_itens = pedido.get("order_itens")
        numero_pedido = pedido.get("order_number")
       
        self.pedidos.append({
            "table_number": mesa.random_table_number,
            "client_name": client_name,
            "order_number": numero_pedido,
            "date": date,
            "order_itens": order_itens
        })

    def enviar_pedido_cozinha(self):
        for pedido in self.pedidos:
            # self.producer.publish(pedido)
            pass


