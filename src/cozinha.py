import threading
from src.cozinheiro import Cozinheiro
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

class CozinhaConsumer:
    def __init__(self, config: dict, consumer: ConsumerRabbitMQ) -> None:
        self.config = config
        self.consumer = consumer
    
    def cozinheiro_thread(self, cozinheiro_id: int):
        cozinheiro = Cozinheiro(cozinheiro_id, self.consumer)
        cozinheiro.comeca_producao()

    def execute(self):
        quantidade_cozinheiros: int = self.config.get("quantidade_cozinheiros")

        print(f"Aguardando Pedidos...")

        for cozinheiro_id in range(quantidade_cozinheiros):
            cozinheiro_id = cozinheiro_id + 1
            thread_cozinheiro = threading.Thread(target=self.cozinheiro_thread, args=(cozinheiro_id,))
            thread_cozinheiro.start()