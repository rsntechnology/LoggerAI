from abc import ABC, abstractmethod
from pydantic import BaseModel

class WebhookPort(ABC):
    @abstractmethod
    def process_webhook(self, data: dict):
        pass