import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)