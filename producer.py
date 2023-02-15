from src.restaurant import Restaurant
from src.adapters.producer_rabbit import ProducerRabbitMQ

settings = {
    "amount_tables": 50,
    "amount_waiters": 1,
    "number_people_per_table": 5
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