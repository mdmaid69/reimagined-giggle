  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()