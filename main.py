import time
def wait_for_seconds(seconds):
        time.sleep(seconds)
def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities