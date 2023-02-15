
from src.kitchen import Kitchen
from src.adapters.consumer_rabbit import ConsumerRabbitMQ
from os import getenv

settings = {
    "amount_cooks":  int(getenv("RESTAURANT_KITCHEN_AMOUNT_COOKS"))
}

consumer_rabbitmq = ConsumerRabbitMQ({
    "queue": "order"
})

cozinha = Kitchen(settings, consumer_rabbitmq)
cozinha.execute()