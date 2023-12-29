def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread