import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
def convert_to_binary(n):
        return bin(n)