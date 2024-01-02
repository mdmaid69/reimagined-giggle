  import sys
  def get_python_version():
        return sys.version
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities