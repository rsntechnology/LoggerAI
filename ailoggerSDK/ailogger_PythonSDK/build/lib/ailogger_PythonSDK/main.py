import logging
import requests
import json
import time

# Configure logging
logging.basicConfig(level=logging.INFO)

class ailogger:
    def __init__(self, webhook_url, application):
        self.logs = []
        self.metrics = []
        self.errors = []
        self.webhook_url = webhook_url
        self.application = application

    def error_exceptions(self, exception):
        # Capture the exception, type, and time
        error_data = {'type': 'error.exception', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': str(exception)}
        self.errors.append(error_data)
        # Log the error for debugging purposes
        logging.error(f"\033[91m{exception}\033[0m")  # Log error in red
        self.send_logs_to_webhook()
        self.errors = []

    def error_application(self, exception):
        # Capture the exception, type, and time
        error_data = {'type': 'error.application', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': str(exception)}
        self.errors.append(error_data)
        # Log the error for debugging purposes
        logging.error(f"\033[91m{exception}\033[0m")  # Log error in red
        self.send_logs_to_webhook()
        self.errors = []

    def log_info(self, message):
        # Log a message, type, and time
        log_data = {'type': 'log.info', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': message}
        self.logs.append(log_data)
        # Log the message for debugging purposes
        logging.info(f"\033[92m{message}\033[0m")  # Log info in green
        # Send logs to webhook
        self.send_logs_to_webhook()
        self.logs = []

    def log_debug(self, message):
        # Log a message, type, and time
        log_data = {'type': 'log.debug', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': message}
        self.logs.append(log_data)
        # Log the message for debugging purposes
        logging.info(f"\033[92m{message}\033[0m")  # Log info in green
        # Send logs to webhook
        self.send_logs_to_webhook()
        self.logs = []

    def log_warning(self, message):
        # Log a message, type, and time
        log_data = {'type': 'log.warning', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': message}
        self.logs.append(log_data)
        # Log the message for debugging purposes
        logging.info(f"\033[92m{message}\033[0m")  # Log info in green
        # Send logs to webhook
        self.send_logs_to_webhook()
        self.logs = []

    def metric(self, name, value):
        metric_data = {'type': 'metric', 'time': time.strftime('%Y-%m-%d %H:%M:%S'), 'message': {name: value}}
        self.metrics.append(metric_data)
        # Log the metric for debugging purposes
        logging.info(f"\033[94mMetric captured: {name} = {value}\033[0m")  # Log metric in blue
        self.send_logs_to_webhook()
        self.metrics = []

    def send_logs_to_webhook(self):
        # Send logs to the webhook
        headers = {'Content-Type': 'application/json'}
        data = {'logs': self.logs, 'metrics': self.metrics, 'errors': self.errors, 'application': self.application}
        try:
            response = requests.post(self.webhook_url, data=json.dumps(data), headers=headers)
            if response.status_code == 200:
                pass
            else:
                logging.error(f"Failed to send logs to webhook. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error occurred while sending logs to webhook: {str(e)}")

