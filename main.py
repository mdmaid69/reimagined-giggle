import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_force(mass, acceleration):
        return mass * acceleration