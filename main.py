def calculate_speed(distance, time):
        return distance / time
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread