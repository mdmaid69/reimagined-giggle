import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)