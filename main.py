  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()