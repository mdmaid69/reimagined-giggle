import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
def calculate_density(mass, volume):
        return mass / volume