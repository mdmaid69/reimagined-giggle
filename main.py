import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread
import random
def generate_random_choice(choices):
        return random.choice(choices)