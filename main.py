import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_acceleration(speed, time):
        return speed / time