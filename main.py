def calculate_work(force, distance):
        return force * distance
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread