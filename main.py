import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_density(mass, volume):
        return mass / volume