def calculate_energy(mass, c=3*10**8):
        return mass * c**2
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread