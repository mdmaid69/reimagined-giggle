import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_acceleration(speed, time):
        return speed / time