def calculate_acceleration(speed, time):
        return speed / time
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread