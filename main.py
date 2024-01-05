import shutil
def delete_directory(path):
        shutil.rmtree(path)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()