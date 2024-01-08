import time
def get_current_time():
        return time.ctime()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"