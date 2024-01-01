  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding