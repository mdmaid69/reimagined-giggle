import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def cube_number(x):
        return x**3