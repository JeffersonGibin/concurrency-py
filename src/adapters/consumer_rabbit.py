import json
from pika import PlainCredentials, BlockingConnection, ConnectionParameters

from src.interfaces.ConsumerInterface import Consumer

class ConsumerRabbitMQ(Consumer):
    def __init__(self, config) -> None:
        self.config = config

    def consumer(self, cb):
        credentials = PlainCredentials('rabbitmq', 'rabbitmq')
        connection = BlockingConnection(ConnectionParameters(host='rabbit', port=5672, credentials=credentials))
        channel = connection.channel()
    
        queue_name = self.config.get("queue")
        channel.queue_declare(queue=queue_name)
        
        channel.basic_consume(queue=self.config.get("queue"), on_message_callback=cb, auto_ack=True)

        channel.start_consuming()
