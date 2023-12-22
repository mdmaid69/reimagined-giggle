  import os
  def delete_file(file_name):
        os.remove(file_name)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()