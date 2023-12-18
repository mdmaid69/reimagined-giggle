import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import random
def roll_die():
        return random.randint(1, 6)