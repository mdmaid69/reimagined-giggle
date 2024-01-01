def calculate_average(lst):
        return sum(lst) / len(lst)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread