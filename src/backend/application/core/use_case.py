from .entities import Loger, Metric, Error
from .repositories import DataRepository

class ProcessWebhookUseCase:
    def __init__(self, data_repository: DataRepository):
        self.data_repository = data_repository

    def execute(self, data: dict):
        # Extract relevant data from the webhook payload
        logs = [Loger(message=message) for message in data.get('logs', [])]
        metrics = [Metric(message=message) for message in data.get('metrics', [])]
        errors = [Error(message=message) for message in data.get('errors', [])]
        
        # Save the extracted data
        for log in logs:
            self.data_repository.save_log(log)
        for metric in metrics:
            self.data_repository.save_metric(metric)
        for error in errors:
            self.data_repository.save_error(error)
