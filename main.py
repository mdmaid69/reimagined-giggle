  def calculate_area_rectangle(l, w):
        return l * w
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))