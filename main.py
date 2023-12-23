import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities