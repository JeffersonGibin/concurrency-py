import math
import random

from src.client import Client

class Table:
    def __init__(self) -> None:
        self.custumers = []
        self.random_table_number = math.ceil(random.randint(1, 15))

    def accommodate_customer(self, custumer: Client) -> None:
        self.custumers.append(custumer)

    def custumers(self) -> list:
        return self.custumers
