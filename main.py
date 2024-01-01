import glob
def find_files(pattern):
        return glob.glob(pattern)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()