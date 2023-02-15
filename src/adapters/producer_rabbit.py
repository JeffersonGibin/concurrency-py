import json
from pika import PlainCredentials, BlockingConnection, ConnectionParameters, exceptions

from src.interfaces.ProducerInterface import Producer

class ProducerRabbitMQ(Producer):
    def __init__(self, settings) -> None:
        self.settings = settings

    def publish(self, payload: dict):

        try:
            # Conecte-se ao servidor RabbitMQ
            credentials = PlainCredentials('rabbitmq', 'rabbitmq')
            connection = BlockingConnection(ConnectionParameters(host='rabbit', port=5672, credentials=credentials, socket_timeout=10))
            channel = connection.channel()
            
        
            if channel:
                # Declaração da Fila de Pedidos
                queue_name = self.settings.get("queue")
                channel.queue_declare(queue=queue_name)
            
                # Envia o Pedido para a Fila
                payload= json.dumps(payload)
                channel.basic_publish(exchange='',
                                    routing_key=self.settings.get("routing_key"),
                                    body=payload)
                connection.close()

        except exceptions.AMQPConnectionError as err:
            print("Could not establish connection to RabbitMQ:", err)
