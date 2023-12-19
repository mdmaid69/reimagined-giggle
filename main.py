import logging
def log_message(message):
        logging.info(message)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time