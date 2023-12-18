  import os
  def get_current_directory():
        return os.getcwd()
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()