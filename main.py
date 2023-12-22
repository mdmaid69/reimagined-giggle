import logging
def setup_logging(level):
        logging.basicConfig(level=level)
def calculate_pressure(force, area):
        return force / area