
import json
import time

from src.adapters.consumer_rabbit import ConsumerRabbitMQ

class Cook:
    def __init__(self, cook_id: int, consumer: ConsumerRabbitMQ) -> None:
        self.cook_id = cook_id
        self.consumer_rabbitmq = consumer

    
    def start_production(self):

        def callback(ch, method, properties, body: str):
            order = json.loads(body.decode())

            if order:
                cook_id = self.cook_id
                order_number = order['order_number']
                table_number = order["table_number"]
                orders = order.get("order_itens")

                print(f"Cook {str(cook_id)} RECEIVE the order N° {order_number} from the table N° {table_number}")


                for product in orders[0]:
                    # Simulate time execution
                    time.sleep(2)
                
                print(f"Cook {cook_id} FINISH the order N° {order_number} from the table N° {table_number}")
            else:
                print("Cook {cook_id} is wait new Orders!!!!")


        self.consumer_rabbitmq.consumer(callback)