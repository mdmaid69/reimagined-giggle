import sys
def add_to_python_path(path):
        sys.path.append(path)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities