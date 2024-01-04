import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()