def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()