import datetime
def get_current_datetime():
        return datetime.datetime.now()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2