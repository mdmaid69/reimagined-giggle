import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list