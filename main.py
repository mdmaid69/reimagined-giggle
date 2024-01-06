  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()