import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def split_path(path):
        return os.path.split(path)