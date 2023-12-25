def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)
import logging
def setup_logging(level):
        logging.basicConfig(level=level)