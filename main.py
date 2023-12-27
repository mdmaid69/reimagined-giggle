  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import time
def get_time_since_epoch():
        return time.time()