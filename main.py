def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import os
def remove_directory(path):
        os.rmdir(path)