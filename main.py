  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()