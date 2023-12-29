  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()