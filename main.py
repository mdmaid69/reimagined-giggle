def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)