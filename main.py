  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))