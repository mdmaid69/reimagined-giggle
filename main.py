  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()