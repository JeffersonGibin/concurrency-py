import threading
import time

from src.custumer import Custumer
from src.waiter import Waiter
from src.table import Table
from src.interfaces.producer_interface import Producer


class Restaurant:
    def __init__(self, settings: dict, producer: Producer) -> None:
        self.threads = []
        self.waiters = []
        self.settings = settings
        self.producer = producer

    def __check_waiter_is_available(self)-> bool:
        return len(self.waiters) > 0 and len(self.waiters) <= self.settings.get("amount_waiters")

    def __waiter_actions(self):
        table, orders_table = self.__create_table_with_people()

        last_waiter_id = len(self.waiters) -1
        waiter: Waiter = self.waiters[last_waiter_id]
        waiter_id = waiter.id

        for order in orders_table:
            data_order = order.get()
            order_number = data_order.get("order_number")

            print(f"[x] Waiter {waiter_id} is taking Order N° {order_number}")
            waiter.write_orders(order, table)

            symbolic_time = 0.0002 * waiter_id
            time.sleep(symbolic_time)

            print(f"[x] Waiter {waiter_id} took the Order N° {order_number}")
            print(f"[x] Waiter {waiter_id} send Order N° {order_number} to the kitchen")
        
        waiter.send_order_to_kitchen()
        time.sleep(1)


    def __request_waiter_thread(self):
        therad = threading.Thread(target=self.__waiter_actions)
        self.threads.append(therad)
        therad.start()


    def __create_waiters(self):
        for waiter_id in range(self.settings.get("amount_waiters")):
            id = waiter_id + 1
            waiter = Waiter(id, self.producer)
            self.waiters.append(waiter)

    def __create_table_with_people(self):
        table = Table()
        orders = []

        for custumer_id in range(self.settings.get("number_people_per_table")):
            custumer_name = "Person "+ str(custumer_id + 1)
            custumer = Custumer(custumer_name)
            table.accommodate_customer(custumer)

            order = custumer.make_order([
                {
                    "product": "Hamburger"
                },
                {
                    "product": "Pizza"
                }
            ])

            orders.append(order)

        return  (table, orders)


    def execute(self):
        amount_tables = self.settings.get("amount_tables")

        self.__create_waiters()
        
        # As long as there are tables:
        while amount_tables > 0:
            
            # And Waiter available then:
            if self.__check_waiter_is_available():
                print("[X] Table N°: ", amount_tables)

                # Necessary calculations
                ONE_TABLE = 1
                amount_tables -= ONE_TABLE

                # Call Thread
                self.__request_waiter_thread()
                
                # Remove a Waiter from the control list
                self.waiters.pop()
            else:
                print("\n\n################################ [UNAVAILABLE WAITERS] ################################")
                print(f"[UNAVAILABLE WAITERS] The Restaurant has no waiter available!")
                print("###########################################################################\n\n")


                for t in self.threads:
                    t.join()

                    # Check if it's thread not running
                    if not t.is_alive():
                        ONE_WAITER = 1

                        self.threads.remove(t)
                        next_waiter_id = len(self.waiters) + ONE_WAITER
                        self.waiters.append(Waiter(next_waiter_id, self.producer))

                        print("\n\n########################### [Releasing Waiter] ###########################")
                        print("[X] Releasing Waiter for new orders")
                        print("###########################################################################\n\n")