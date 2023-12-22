import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]