import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def reverse_string(s):
        return s[::-1]