  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  def remove_duplicates(lst):
        return list(set(lst))