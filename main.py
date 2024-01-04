import logging
def log_message(message):
        logging.info(message)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)