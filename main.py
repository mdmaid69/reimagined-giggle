import datetime
def get_current_date():
        return datetime.date.today()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"