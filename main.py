import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import random
def generate_random_choice(choices):
        return random.choice(choices)