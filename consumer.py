
from src.adapter.broker_rabbitmq import BrokerRabbitMQAdapter
from src.kitchen import Kitchen
from src.repositories.consumer_rabbit import ConsumerRabbitMQRepository
from os import getenv

settings = {
    "amount_cooks":  int(getenv("RESTAURANT_KITCHEN_AMOUNT_COOKS"))
}

# Instance Adapter
adapter = BrokerRabbitMQAdapter({
    'user': 'rabbitmq',
    'password': 'rabbitmq',
    'host': 'rabbit',
    'port': 5672,
})

consumer_rabbitmq = ConsumerRabbitMQRepository({
    "queue": "order",
}, adapter)

cozinha = Kitchen(settings, consumer_rabbitmq)
cozinha.execute()
