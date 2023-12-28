  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities