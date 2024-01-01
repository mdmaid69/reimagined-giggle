  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()