from src.pedido import Pedido


class Cliente:
    def __init__(self, cliente) -> None:
        self.cliente = cliente
    
    def realiza_pedido(self, dados_pedido: dict) -> Pedido:
        cliente: dict = self.cliente
        pedido =  Pedido({
            "cliente": cliente,
            "pedido": dados_pedido,
        })

        return pedido