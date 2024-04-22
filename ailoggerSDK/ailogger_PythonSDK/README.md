## AI Logger Python SDK

```markdown
# AI Logger

AI Logger is a Python library for logging and monitoring errors and events in your application.

## Features

- Log exceptions and application errors with `error_exception` and `error_application` methods.
- Log informational and debug messages with `log_info` and `log_debug` methods.
- Automatically sends logs to a configured webhook.

## Installation

You can install AI Logger with pip:

pip install ailogger

```

## Usage

Here's a basic example of how to use AI Logger:

```python

# Import necessary modules
import ailogger_PythonSDK as salogger

# Define the webhook URL 
webhook_url = 'http://127.0.0.1:8000/webhook'

# Start data monitoring with the webhook URL
ailogging = salogger.ailogger(webhook_url, 'sample')

# Function to simulate errors, logs, and metrics in your application

try:
    # Simulate an error
    1 / 0
except Exception as e:
    # Capture the exception using ErrorMonitoring
    ailogging.error_exceptions(e)

ailogging.error_application("issue in the application")

# Simulate logging a message
ailogging.log_info("This is a log message")

# Simulate capturing metrics
ailogging.metric("metric1", 100)
ailogging.metric("metric2", 200)

```

## Requirements

- Python 3.6 or later

## License

This project is licensed under the MIT License.

## Contact

If you have any questions, feel free to contact me at your.email@example.com.
