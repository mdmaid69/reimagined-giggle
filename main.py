def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)