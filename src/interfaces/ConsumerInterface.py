from abc import ABC, abstractmethod

class Consumer(ABC):

    @abstractmethod
    def consumer(self, cb):
        pass