  import datetime
  def get_current_date():
        return datetime.datetime.now().date()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities