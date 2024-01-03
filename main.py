import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities