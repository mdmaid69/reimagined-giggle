import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities