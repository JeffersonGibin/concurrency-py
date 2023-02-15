
from src.cozinha import CozinhaConsumer
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

config = {
    "amount_cooks": 5
}

consumer_rabbitmq = ConsumerRabbitMQ({
    "queue": "order"
})

cozinha = CozinhaConsumer(config, consumer_rabbitmq)
cozinha.execute()