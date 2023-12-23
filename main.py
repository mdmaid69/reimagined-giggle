def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value