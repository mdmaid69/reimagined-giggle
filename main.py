import datetime
def get_today_date():
        return datetime.date.today()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"