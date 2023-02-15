import json
from pika import PlainCredentials, BlockingConnection, ConnectionParameters, exceptions

from src.interfaces.ConsumerInterface import Consumer

class ConsumerRabbitMQ(Consumer):
    def __init__(self, settings) -> None:
        self.settings = settings

    def consumer(self, cb):
        try:
            credentials = PlainCredentials('rabbitmq', 'rabbitmq')
            connection = BlockingConnection(ConnectionParameters(host='rabbit', port=5672, credentials=credentials, socket_timeout=10))
            channel = connection.channel()

            queue_name = self.settings.get("queue")
            channel.queue_declare(queue=queue_name)
            
            channel.basic_consume(queue=self.settings.get("queue"), on_message_callback=cb, auto_ack=True)

            channel.start_consuming()
            
        except exceptions.AMQPConnectionError as err:
            print("Could not establish connection to RabbitMQ:", err)
