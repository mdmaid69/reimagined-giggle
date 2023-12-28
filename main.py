import logging
def log_message(message):
        logging.info(message)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time