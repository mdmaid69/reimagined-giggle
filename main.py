import logging
def log_message(message):
        logging.info(message)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time