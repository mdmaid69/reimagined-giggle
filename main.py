import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity