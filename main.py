import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_work(force, distance):
        return force * distance