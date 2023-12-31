import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)