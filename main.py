import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_speed(distance, time):
        return distance / time