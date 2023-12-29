  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()