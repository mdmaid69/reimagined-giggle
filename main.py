  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()