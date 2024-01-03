import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
  def remove_duplicates(lst):
        return list(set(lst))