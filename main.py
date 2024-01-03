  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue