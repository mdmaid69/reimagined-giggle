import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)