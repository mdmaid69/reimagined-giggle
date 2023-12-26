def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import logging
def setup_logging(level):
        logging.basicConfig(level=level)