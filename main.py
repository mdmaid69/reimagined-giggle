import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities