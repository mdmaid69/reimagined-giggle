import datetime
def get_current_datetime():
        return datetime.datetime.now()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"