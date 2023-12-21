import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()