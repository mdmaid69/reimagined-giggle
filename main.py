import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time