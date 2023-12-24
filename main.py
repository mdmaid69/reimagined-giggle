import logging
def log_message(message):
        logging.info(message)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)