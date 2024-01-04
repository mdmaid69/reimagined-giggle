import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities