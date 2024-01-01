import logging
def log_message(message):
        logging.info(message)
def calculate_energy(mass, c=3*10**8):
        return mass * c**2