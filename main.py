def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import logging
def log_message(message):
        logging.info(message)