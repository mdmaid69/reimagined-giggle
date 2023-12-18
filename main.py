import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities