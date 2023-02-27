from src.adapter.broker_rabbitmq import BrokerRabbitMQAdapter
from src.restaurant import Restaurant
from src.repositories.producer_rabbit import ProducerRabbitMQRepository
from os import getenv

settings = {
    "amount_tables": int(getenv("RESTAURANT_AMOUNT_TABLES")),
    "amount_waiters": int(getenv("RESTAURANT_AMOUNT_WAITERS")),
    "number_people_per_table": int(getenv("RESTAURANT_NUMBER_PEOPLE_PER_TABLE")),
}

print("Settings Execution")
print(f"[X] Amount Tables: {settings['amount_tables']}")
print(f"[X] Amount Waiters: {settings['amount_waiters']}")
print(
    f"[X] Amount People per table: {settings['number_people_per_table']}\n\n")


# Instance Adapter
adapter = BrokerRabbitMQAdapter({
    'user': 'rabbitmq',
    'password': 'rabbitmq',
    'host': 'rabbit',
    'port': 5672,
})

producer = ProducerRabbitMQRepository({
    "queue": "order",
    "routing_key": "order"
}, adapter)

restaurante = Restaurant(settings, producer)
restaurante.execute()
