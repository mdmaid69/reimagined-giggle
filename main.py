import array
def write_array_to_file(filename, array):
        with open(filename, "wb") as f:
        array.tofile(f)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()