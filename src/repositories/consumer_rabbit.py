from pika import exceptions
from src.interfaces.broker_interface import Broker
from src.interfaces.consumer_interface import Consumer

class ConsumerRabbitMQRepository(Consumer):
    def __init__(self, settings, broker: Broker) -> None:
        self.settings = settings
        self.broker = broker

    def consumer(self, cb):
        try:
            channel = self.broker.connection()

            queue_name = self.settings.get("queue")
            channel.queue_declare(queue=queue_name)
            
            channel.basic_consume(queue=self.settings.get("queue"), on_message_callback=cb, auto_ack=True)

            channel.start_consuming()
            
        except exceptions.AMQPConnectionError as err:
            print(err)
            print("Could not establish connection to RabbitMQ:", err)
