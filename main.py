  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()