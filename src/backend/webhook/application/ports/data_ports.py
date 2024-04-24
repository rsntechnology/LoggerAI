from abc import ABC, abstractmethod

class DataPort(ABC):
    @abstractmethod
    def retrieve_data(self, data_type: str, application: str):
        pass
