
from src.cozinha import CozinhaConsumer
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

config = {
    "quantidade_cozinheiros": 5
}

consumer_rabbitmq = ConsumerRabbitMQ({
    "queue": "pedido"
})

cozinha = CozinhaConsumer(config, consumer_rabbitmq)
cozinha.execute()