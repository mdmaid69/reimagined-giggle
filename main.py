  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())