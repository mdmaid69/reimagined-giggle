import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import array
def iterate_over_array(array):
        for item in array:
        print(item)