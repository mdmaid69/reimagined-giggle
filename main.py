  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"