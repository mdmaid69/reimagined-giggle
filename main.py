def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())