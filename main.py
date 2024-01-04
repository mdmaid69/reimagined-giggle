import multiprocessing
def get_cpu_count():
        return multiprocessing.cpu_count()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"