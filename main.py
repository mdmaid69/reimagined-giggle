import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"