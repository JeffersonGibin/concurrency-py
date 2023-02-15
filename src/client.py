from src.order import Order


class Client:
    def __init__(self, cliente) -> None:
        self.cliente = cliente
    
    def realiza_pedido(self, dados_pedido: dict) -> Order:
        cliente: dict = self.cliente
        pedido =  Order({
            "cliente": cliente,
            "pedido": dados_pedido,
        })

        return pedido