import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_equity_ratio(total_equity, total_assets):
        return total_equity / total_assets