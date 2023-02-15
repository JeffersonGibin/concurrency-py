
from src.kitchen import Kitchen
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

settings = {
    "amount_cooks": 5
}

consumer_rabbitmq = ConsumerRabbitMQ({
    "queue": "order"
})

cozinha = Kitchen(settings, consumer_rabbitmq)
cozinha.execute()