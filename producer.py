from src.restaurant import Restaurant
from src.adapters.producer_rabbit import ProducerRabbitMQ
from os import getenv

settings = {
    "amount_tables": int(getenv("RESTAURANT_AMOUNT_TABLES")),
    "amount_waiters": int(getenv("RESTAURANT_AMOUNT_WAITERS")),
    "number_people_per_table": int(getenv("RESTAURANT_NUMBER_PEOPLE_PER_TABLE")),
}

print("Settings Execution")
print(f"[X] Amount Tables: {settings['amount_tables']}")
print(f"[X] Amount Waiters: {settings['amount_waiters']}")
print(f"[X] Amount People per table: {settings['number_people_per_table']}\n\n")

producer = ProducerRabbitMQ({
    "queue": "order",
    "routing_key": "order"
})

restaurante = Restaurant(settings, producer)
restaurante.execute()