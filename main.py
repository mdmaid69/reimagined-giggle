  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps