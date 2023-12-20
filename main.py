def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import glob
def find_files(pattern):
        return glob.glob(pattern)