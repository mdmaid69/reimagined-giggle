import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_energy(mass, c=3*10**8):
        return mass * c**2