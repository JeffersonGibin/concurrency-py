import json
from pika import exceptions
from src.interfaces.broker_interface import Broker

from src.interfaces.producer_interface import Producer


class ProducerRabbitMQRepository(Producer):
    def __init__(self, settings, broker: Broker) -> None:
        self.settings = settings
        self.broker = broker

    def publish(self, payload: dict):

        try:
            channel = self.broker.connection()

            if channel:
                # Declaração da Fila de Pedidos
                queue_name = self.settings.get("queue")
                channel.queue_declare(queue=queue_name)

                # Envia o Pedido para a Fila
                payload = json.dumps(payload)
                channel.basic_publish(exchange='',
                                      routing_key=self.settings.get(
                                          "routing_key"),
                                      body=payload)
                channel.close()

        except exceptions.AMQPConnectionError as err:
            print("Could not establish connection to RabbitMQ:", err)
