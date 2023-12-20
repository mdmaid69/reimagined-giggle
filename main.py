import threading

def print_hello():
        print("Hello, world!")

thread = threading.Thread(target=print_hello)
thread.start()
thread.join()
def find_difference(list1, list2):
        return set(list1) - set(list2)