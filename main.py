  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities