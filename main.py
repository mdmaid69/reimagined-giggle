  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()