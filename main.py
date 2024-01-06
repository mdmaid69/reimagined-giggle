  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps