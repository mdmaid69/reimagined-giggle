import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue