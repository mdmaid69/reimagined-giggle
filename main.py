def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"