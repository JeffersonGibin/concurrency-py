from abc import ABC, abstractmethod

class Broker(ABC):

    @abstractmethod
    def connection(self)->any:
        pass