from src.restaurante_producer import RestauranteProducer
from src.adapters.producer_rabbit import ProducerRabbitMQ

config = {
    "amount_tables": 50,
    "amount_waiters": 1,
    "number_people_per_table": 5
}

print("Config Execution")
print(f"[X] Amount Tables: {config['amount_tables']}")
print(f"[X] Amount Waiters: {config['amount_waiters']}")
print(f"[X] Amount People per table: {config['number_people_per_table']}\n\n")

producer = ProducerRabbitMQ({
    "queue": "order",
    "routing_key": "order"
})

restaurante = RestauranteProducer(config, producer)
restaurante.execute()