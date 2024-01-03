import time
def get_current_time():
        return time.ctime()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2