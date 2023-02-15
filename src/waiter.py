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
        cliente = pedido.get("cliente")
        data = pedido.get("data")
        dados_pedido = pedido.get("pedido")
        numero_pedido = pedido.get("numero_pedido")
       
        self.pedidos.append({
            "mesa": mesa.mesa_id,
            "cliente": cliente,
            "numero_pedido": numero_pedido,
            "data": data,
            "pedido": dados_pedido
        })

    def enviar_pedido_cozinha(self):
        for pedido in self.pedidos:
            # self.producer.publish(pedido)
            pass


