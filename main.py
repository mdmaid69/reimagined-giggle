import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)