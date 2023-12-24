  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets