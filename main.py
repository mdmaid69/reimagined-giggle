import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()