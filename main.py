import time
def get_time_since_epoch():
        return time.time()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2