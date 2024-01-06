import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)