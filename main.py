def calculate_force(mass, acceleration):
        return mass * acceleration
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread