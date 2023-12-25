  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps