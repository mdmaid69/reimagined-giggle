import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import threading
def create_thread(target):
        thread = threading.Thread(target=target)
        thread.start()
        return thread