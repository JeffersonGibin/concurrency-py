import threading
from src.cook import Cook
from src.adapters.consumer_rabbit import ConsumerRabbitMQ

class Kitchen:
    def __init__(self, config: dict, consumer: ConsumerRabbitMQ) -> None:
        self.config = config
        self.consumer = consumer
    
    def cook_thread(self, cook_id: int):
        cook = Cook(cook_id, self.consumer)
        cook.start_production()

    def execute(self):
        amount_cooks: int = self.config.get("amount_cooks")

        print(f"Wait Orders...")

        for cook_id in range(amount_cooks):
            cook_id = cook_id + 1
            thread = threading.Thread(target=self.cook_thread, args=(cook_id,))
            thread.start()