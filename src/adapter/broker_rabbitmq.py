
from src.interfaces.broker_interface import Broker
from pika import PlainCredentials, BlockingConnection, ConnectionParameters


class BrokerRabbitMQAdapter(Broker):
    def __init__(self, settings) -> None:
        super()

        self.settings = settings
        self.blocking_connection = None

    def connection(self):
        credentials = PlainCredentials(self.settings.get(
            "user"), self.settings.get("password"))
        self.blocking_connection = BlockingConnection(ConnectionParameters(host=self.settings.get(
            "host"), port=self.settings.get("port"), credentials=credentials, socket_timeout=10))
        return self.blocking_connection.channel()

