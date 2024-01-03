  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import time
def wait_for_seconds(seconds):
        time.sleep(seconds)