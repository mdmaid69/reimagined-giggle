  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()