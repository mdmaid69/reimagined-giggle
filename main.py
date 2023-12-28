import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_roi(gain, cost):
        return (gain - cost) / cost