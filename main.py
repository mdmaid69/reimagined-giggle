import random
def flip_coin():
        return "Heads" if random.random() < 0.5 else "Tails"
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()