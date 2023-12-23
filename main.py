  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue