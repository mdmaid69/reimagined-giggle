import random
def roll_die():
        return random.randint(1, 6)
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread