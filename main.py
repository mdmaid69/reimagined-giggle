  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()