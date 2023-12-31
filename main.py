  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()