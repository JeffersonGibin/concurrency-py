from src.restaurante_producer import RestauranteProducer
from src.adapters.producer_rabbit import ProducerRabbitMQ

config = {
    "quantidade_mesas": 50,
    "quantidade_garcons": 1,
    "quantidade_pessoas_por_mesa": 5
}

print("Configuração da execução")
print(f"[X] Quantidade de Mesas: {config['quantidade_mesas']}")
print(f"[X] Quantidade de Garçons: {config['quantidade_garcons']}")
print(f"[X] Quantidade de Pessoas Por Mesa: {config['quantidade_pessoas_por_mesa']}\n\n")

producer = ProducerRabbitMQ({
    "queue": "pedido",
    "routing_key": "pedido"
})

restaurante = RestauranteProducer(config, producer)
restaurante.execute()