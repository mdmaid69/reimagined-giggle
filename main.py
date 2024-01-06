  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"