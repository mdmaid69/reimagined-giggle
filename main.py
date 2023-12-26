import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets