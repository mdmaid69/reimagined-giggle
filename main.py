def calculate_area(radius):
        return 3.14 * radius * radius
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread