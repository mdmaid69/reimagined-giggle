import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"