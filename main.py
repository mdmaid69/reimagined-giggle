  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()