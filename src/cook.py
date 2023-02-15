
import json
import time

from src.adapters.consumer_rabbit import ConsumerRabbitMQ

class Cook:
    def __init__(self, cozinheiro_id: int, consumer: ConsumerRabbitMQ) -> None:
        self.cozinheiro_id = cozinheiro_id
        self.consumer_rabbitmq = consumer

    
    def comeca_producao(self):

        def callback(ch, method, properties, body: str):
            pedido = json.loads(body.decode())

            if pedido:
                identificacao_cozinheiro = self.cozinheiro_id
                numero_pedido = pedido['numero_pedido']
                numero_mesa = pedido["mesa"]
                dados_pedidos = pedido.get("pedido")

                print(f"Cozinheiro {str(identificacao_cozinheiro)} RECEBEU o pedido N° {numero_pedido} da mesa N° {numero_mesa}")


                for produto in dados_pedidos[0]:
                    # Simula tempo de produção
                    time.sleep(2)
                
                print(f"Cozinheiro {identificacao_cozinheiro} TERMINOU o pedido N° {numero_pedido} da mesa N° {numero_mesa}")
            else:
                print("Cozinheiro {identificacao_cozinheiro} está aguardando novos pedidos!!!!")


        self.consumer_rabbitmq.consumer(callback)