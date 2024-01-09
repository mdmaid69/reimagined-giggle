def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread