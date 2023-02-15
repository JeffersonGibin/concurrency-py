
from src.kitchen import Kitchen
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

config = {
    "amount_cooks": 5
}

consumer_rabbitmq = ConsumerRabbitMQ({
    "queue": "order"
})

cozinha = Kitchen(config, consumer_rabbitmq)
cozinha.execute()