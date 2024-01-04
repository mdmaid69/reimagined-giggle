  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()