def calculate_volume(length, width, height):
        return length * width * height
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread