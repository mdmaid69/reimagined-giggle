def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")