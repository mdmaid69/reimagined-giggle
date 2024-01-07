def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread