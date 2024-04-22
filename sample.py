# Import necessary modules
import ailogger_PythonSDK as salogger

# Define the webhook URL (replace it with your generated URL from RequestBin)
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
