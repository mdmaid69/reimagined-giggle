import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_force(mass, acceleration):
        return mass * acceleration