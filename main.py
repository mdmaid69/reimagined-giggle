import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def calculate_area(radius):
        return 3.14 * radius * radius