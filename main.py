  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()