import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_density(mass, volume):
        return mass / volume