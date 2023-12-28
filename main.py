import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
def calculate_energy(mass, c=3*10**8):
        return mass * c**2