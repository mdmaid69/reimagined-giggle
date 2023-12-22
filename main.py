import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities