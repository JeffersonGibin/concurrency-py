import json
from pika import PlainCredentials, BlockingConnection, ConnectionParameters

from src.interfaces.ProducerInterface import Producer

class ProducerRabbitMQ(Producer):
    def __init__(self, settings) -> None:
        self.settings = settings

    def publish(self, payload: dict):
         # Conecte-se ao servidor RabbitMQ
        credentials = PlainCredentials('rabbitmq', 'rabbitmq')
        connection = BlockingConnection(ConnectionParameters(host='rabbit', port=5672, credentials=credentials))
        channel = connection.channel()
        
        # Declaração da Fila de Pedidos
        queue_name = self.settings.get("queue")
        channel.queue_declare(queue=queue_name)
        
        # Envia o Pedido para a Fila
        payload= json.dumps(payload)
        channel.basic_publish(exchange='',
                            routing_key=self.settings.get("routing_key"),
                            body=payload)
        connection.close()
