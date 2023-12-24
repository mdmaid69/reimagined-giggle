def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import shutil
def move_file(src, dst):
        shutil.move(src, dst)