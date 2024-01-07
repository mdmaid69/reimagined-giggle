import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()