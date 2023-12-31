def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import datetime
def get_current_datetime():
        return datetime.datetime.now()